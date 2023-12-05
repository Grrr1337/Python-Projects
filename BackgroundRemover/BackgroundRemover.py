import os
import io
from rembg import remove
from PIL import Image

"""
NOTE:
This is a wrapper for removing the background of multiple images, contained within a folder (folder_path),
the output is saved in the folder 'dest_path'
"""
class BackgroundRemover:
    def __init__(self, folder_path, dest_path):
        self.folder_path = folder_path
        self.dest_path = dest_path
        self.processed_images = []

    def remove_background_and_save(self):
        # Ensure the destination folder exists
        if not os.path.exists(self.dest_path):
            os.makedirs(self.dest_path)

        # Get a list of all files in the source folder
        file_list = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

        for file_name in file_list:
            # Construct the full path for the input and output files
            input_path = os.path.join(self.folder_path, file_name)
            output_path = os.path.join(self.dest_path, f"{os.path.splitext(file_name)[0]}.png")

            # Open the input image
            with open(input_path, "rb") as input_file:
                # Use rembg to remove the background
                output_data = remove(input_file.read())

                # Convert the output data to an image and save it as a PNG
                output_image = Image.open(io.BytesIO(output_data))
                output_image.save(output_path, format="PNG")

                # Append the processed image path to the list
                self.processed_images.append(output_path)

            # print(f"Background removed and saved: {output_path}")
        # for
    # def remove_background_and_save(self)
# class BackgroundRemover