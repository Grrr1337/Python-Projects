
from ImageComparator import ImageComparator, RenameMode
"""
Sample use for 'ImageComparator'
"""
if __name__ == '__main__':
    # Example usage
    # Return only up to 3 results (AND boolean)
    comparator1 = ImageComparator(needle_image_path='needle.jpg', folder_path='images_to_find', max_hamming_distance=15, top_results=3, target_folder='images_found_1')
    comparator1.copy_results_to_new_folder()
    # comparator1.rename_images_with_hamming_distance()
    comparator1.rename_images_with_hamming_distance(mode=RenameMode.PREFIX)
    # mode ='prefix'

    # Return only up to 5 results
    comparator2 = ImageComparator(needle_image_path='needle.jpg', folder_path='images_to_find', max_hamming_distance=None, top_results=5, target_folder='images_found_2')
    comparator2.copy_results_to_new_folder()
    # comparator2.rename_images_with_hamming_distance()
    comparator2.rename_images_with_hamming_distance(mode=RenameMode.PREFIX)

    # Return all results from 'images_to_find'
    comparator3 = ImageComparator(needle_image_path='needle.jpg', folder_path='images_to_find', max_hamming_distance=None, top_results=None, target_folder='images_found_3')
    comparator3.copy_results_to_new_folder()
    comparator3.copy_results_to_new_folder(target_folder='images_found_3 (2)')
    # comparator3.rename_images_with_hamming_distance()
    comparator3.rename_images_with_hamming_distance(mode=RenameMode.PREFIX) # this mode applies only to the target_folder, provided in the ImageComparator's constructor
# if __name__ == '__main__'
