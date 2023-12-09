import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

"""
File Organizer Script

This script allows the user to organize files in a selected folder based on their extensions.
It utilizes the Tkinter library for a graphical user interface to prompt the user to select a folder.
Author: Vladimir Balabanov, aka. Grrr1337

Usage:
- Run this script, and a dialog box will appear to select a folder.
- Files in the selected folder will be organized into subfolders based on their extensions.

Note: Ensure that Tkinter is installed in your Python environment.

"""
# Function to organize files in a selected folder based on their extensions
def OrganizeFiles():

    # Prompt the user to select a folder using a dialog box
    path = askdirectory(title='Select Folder')  # shows dialog box and returns the path

    # Check if the user provided a valid folder path
    if path == None:
        raise Exception("•••~No Folder was specified !~•••")
    elif not os.path.isdir(path):
        raise Exception("•••~Invalid directory provided !~•••")
    elif not os.path.exists(path):
        raise Exception("•••~The directory does not exist !~•••")

    # Get a list of files in the selected folder
    files = os.listdir(path)

    # Iterate through each file in the folder
    for file in files:
        # Split the filename and extension
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the dot from the extension

        # Check if a folder for the extension already exists
        if os.path.exists(path + '/' + extension):
            # Move the file to the existing extension folder
            shutil.move(path + '/' + file, path+'/'+extension + '/' + file)
        else:
            # Create a new folder for the extension and move the file
            os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

    # Print a message indicating that the organization is complete
    print("Done!")
    return

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the OrganizeFiles function when the script is executed
    OrganizeFiles()
