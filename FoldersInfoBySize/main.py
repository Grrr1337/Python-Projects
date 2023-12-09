
# FoldersInfoBySize
import os
from tkinter.filedialog import askdirectory
import enum

"""
FoldersInfoBySize - A Python program to list folders within a selected parent folder,
                    sorted by their size in descending order.

Description:
This program prompts the user to select a parent folder using a graphical dialog.
It then traverses the directory structure, calculates the size of each folder,
and displays the folders sorted by size in a specified unit (BYTES, KB, MB, or GB).
The user can customize the size unit as needed. The program utilizes the Tkinter library
for the folder selection dialog.

Usage:
1. Run the script.
2. A graphical dialog will prompt you to select a parent folder.
3. The program will display the folders within the selected parent folder, sorted
   by their size in the specified unit (default is MB) in descending order.

Author: Vladimir Balabanov
Date: 12.2023
"""

# Enum for size units
class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4

def convert_unit(size_in_bytes, unit):
    """Convert the size from bytes to other units like KB, MB, or GB"""
    if unit == SIZE_UNIT.KB:
        return size_in_bytes / 1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes / (1024 * 1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes / (1024 * 1024 * 1024)
    else:
        return size_in_bytes

def get_folder_size(folder_path, size_type=SIZE_UNIT.BYTES):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return convert_unit(total_size, size_type)

def list_folders_by_size(parent_folder, size_type=SIZE_UNIT.BYTES):
    folders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]
    folders.sort(key=lambda f: get_folder_size(os.path.join(parent_folder, f), size_type), reverse=True)
    return folders

def main():
    path = askdirectory(title='Select Folder')

    if not path:
        print("Folder selection canceled.")
        return

    size_type = SIZE_UNIT.MB  # You can change this to KB, MB, or GB as needed
    folders = list_folders_by_size(path, size_type)

    print(f"Folders sorted by size ({size_type.name}):")
    for folder in folders:
        folder_path = os.path.join(path, folder)
        size = get_folder_size(folder_path, size_type)
        print(f"{folder}: {size:.2f} {size_type.name}")

if __name__ == "__main__":
    main()
