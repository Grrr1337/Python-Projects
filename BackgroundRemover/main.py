
 
from BackgroundRemover import BackgroundRemover

"""
The goal of this project is to remove the background from an image and save it in .png format.
Sample use for 'BackgroundRemover' -
"""
if __name__ == '__main__': 
    folder_path = "source_images"
    dest_path = "out_images"

    background_remover = BackgroundRemover(folder_path, dest_path)
    background_remover.remove_background_and_save()

    # Access the list of processed images
    print("Processed Images:")
    for processed_image in background_remover.processed_images:
        print(processed_image)
# if __name__ == '__main__'


