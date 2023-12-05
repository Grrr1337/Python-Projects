import os
import shutil
from enum import Enum
from PIL import Image
import DHash

"""
NOTE:
This is a wrapper for searching an image needle(needle_image_path) in a haystack (folder_path).
The actual image comparsion algorithm is forked from here:
https://github.com/hjaurum/DHash.git
"""
class RenameMode(Enum):
    SUFFIX = 'suffix'
    PREFIX = 'prefix'

class ImageComparator:
    def __init__(self, needle_image_path, folder_path, max_hamming_distance, top_results, target_folder):
        """
        Initialize the ImageComparator object with parameters.

        :param needle_image_path: Path to the source image.
        :param folder_path: Path to the folder containing images to be compared.
        :param max_hamming_distance: Maximum Hamming distance allowed for images to be considered similar.
        :param top_results: Number of top results to retrieve. If None, retrieve all results.
        :param target_folder: Path to the target folder where similar images will be copied.
        """
        self.needle_image_path = needle_image_path
        self.folder_path = folder_path
        self.max_hamming_distance = max_hamming_distance
        self.top_results = top_results
        self.target_folder = target_folder
        self.sorted_results = None  # Store sorted results

    def get_similarity(self):
        """
        Compare the source image with all images in the specified folder based on their perceptual similarity using DHash.
        
        :return: A dictionary with image paths as keys and their Hamming distances as values, sorted in ascending order.
        """
        # Read the source image
        src_image = Image.open(self.needle_image_path)
        src_hash = DHash.DHash.calculate_hash(src_image)

        # Initialize the result dictionary
        similarity_results = {}

        # Iterate over all images in the folder
        for filename in os.listdir(self.folder_path):
            target_image_path = os.path.join(self.folder_path, filename)

            # Skip non-image files
            if not target_image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            # Read the target image
            target_image = Image.open(target_image_path)

            # Compute DHash for the target image
            target_hash = DHash.DHash.calculate_hash(target_image)

            # Calculate Hamming distance between DHash values
            hamming_distance = DHash.DHash.hamming_distance(src_hash, target_hash)

            # Store the result in the dictionary
            similarity_results[target_image_path] = hamming_distance

        # Sort the dictionary by Hamming distances in ascending order
        self.sorted_results = {k: v for k, v in sorted(similarity_results.items(), key=lambda item: item[1])}

        # Limit the number of top results if specified
        if self.top_results is not None:
            self.sorted_results = dict(list(self.sorted_results.items())[:self.top_results])

        # Print the sorted results
        # for target_path, distance in self.sorted_results.items():
        #     print(f"Image: {target_path}, Hamming distance: {distance}")

        return self.sorted_results

    def rename_images_with_hamming_distance(self, mode=RenameMode.SUFFIX):
        """
        Rename each image in the target folder with a suffix or prefix indicating its Hamming distance.

        :param mode: Mode for adding Hamming distance to filenames. Can be 'suffix' or 'prefix'.
        """
        # Ensure that the target folder exists
        if not os.path.exists(self.target_folder):
            print(f"Target folder '{self.target_folder}' does not exist.")
            return

        # Iterate over images in the target folder
        for filename in os.listdir(self.target_folder):
            image_path = os.path.join(self.target_folder, filename)

            # Skip non-image files
            if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            # Extract Hamming distance from the sorted results using the filename as key
            _, file_extension = os.path.splitext(filename)
            key = self.folder_path + "\\" + filename
            hamming_distance = str(self.sorted_results.get(key, ''))

            # print(f"key: {key} | hamming_distance: {hamming_distance}")

            # Construct the new target filename with the Hamming distance
            if mode == RenameMode.SUFFIX: # mode == 'suffix':
                # print('SFX')
                new_filename = self.append_suffix(os.path.basename(image_path), hamming_distance)
            elif mode == RenameMode.PREFIX: # mode == 'prefix':
                # print('PREFIX')
                new_filename = self.append_prefix(os.path.basename(image_path), hamming_distance)
            else:
                # print(f"Invalid mode '{mode}'. Please use 'suffix' or 'prefix'.")
                print(f"Invalid mode '{mode}'. Please use RenameMode.SUFFIX or RenameMode.PREFIX.")
                return

            new_image_path = os.path.join(self.target_folder, new_filename)

            # Rename the image
            os.rename(image_path, new_image_path)

    @staticmethod
    def append_suffix(filename, suffix):
        """
        Append a suffix to a filename while preserving its extension.

        :param filename: Original filename.
        :param suffix: Suffix to be appended.
        :return: New filename with the suffix.
        """
        name, ext = os.path.splitext(filename)
        return "{name}_{sfx}{ext}".format(name=name, sfx=suffix, ext=ext)

    @staticmethod
    def append_prefix(filename, prefix):
        # print('filename:', filename)
        """
        Prepend a prefix to a filename while preserving its extension.

        :param filename: Original filename.
        :param prefix: Prefix to be prepended.
        :return: New filename with the prefix.
        """
        # name, ext = os.path.splitext(filename)
        # return "{pre}_{name}{ext}".format(pre=prefix, name=name, ext=ext)
        return "{prefix}_{filename}".format(prefix=prefix, filename=filename)
    
    def copy_results_to_new_folder(self,  target_folder=None):
        """
        Function to copy the results of the similar images. Calls the copy_similar_images method and prints the results.
        """
        if target_folder is None:
            target_folder = self.target_folder

        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Ensure that the paths exist and are correct
        if os.path.exists(self.needle_image_path) and os.path.exists(self.folder_path):
            # Copy similar images based on the max Hamming distance
            self.copy_similar_images(target_folder=target_folder)

            print(f"\nImages copied to {target_folder}")
        else:
            print("Invalid paths. Please provide correct paths to the source image and the folder.")

    
    def copy_similar_images(self, target_folder=None):
        """
        Copy images from the similarity results to a target folder based on a maximum Hamming distance threshold.
        """

        if target_folder is None:
            target_folder = self.target_folder
        
        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Get similarity results
        similarity_results = self.get_similarity()

        # Copy the filtered images to the target folder
        for source_path, hamming_distance in self.sorted_results.items():
            # Construct the target path in the target folder with the Hamming distance suffix
            # target_filename = self.append_suffix(os.path.basename(source_path), hamming_distance)
            target_filename = os.path.basename(source_path)
            target_path = os.path.join(target_folder, target_filename)

            # Copy the image
            shutil.copy2(source_path, target_path)
