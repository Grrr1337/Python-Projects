import os
import shutil
import tkinter
from tkinter import Tk
import customtkinter
from pytube import YouTube
import re 
import time

# python -m pip install git+https://github.com/pytube/pytube
# pip install pytube

# https://github.com/TomSchimansky/CustomTkinter
# pip3 install customtkinter
# pip3 install packaging


def get_downloads_directory():
    # Use os.path.expanduser to expand the ~ in the path (if present)
    user_home = os.path.expanduser("~")

    # Join the user's home directory with the standard downloads directory
    downloads_directory = os.path.join(user_home, "Downloads")

    return downloads_directory

def on_progress(stream, chunk, bytes_remaining, pPercentage, progressBar):
    total_size = stream.filesize
    if (total_size > 0):
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = (bytes_downloaded / total_size) * 100
        per = str(int(percentage_of_completion))
        pPercentage.configure(text=per + '%')
        pPercentage.update()
        # print(per)

        # Update the progress bar
        progressBar.set(float(percentage_of_completion) / 100)

# NOTE: checked in the docs
# https://readthedocs.org/projects/python-pytube/downloads/pdf/stable/
def on_complete(stream, file_path, pPercentage, progressBar):
    time.sleep(1) # delay for 1 sec, just for the user to see that the download is completed
    pPercentage.configure(text='0%')
    pPercentage.update()
    progressBar.set(0.0)

def startDownload(link_entry, status_label, pPercentage, progressBar):
    link = link_entry.get()  # Assuming 'link' is the name of the entry widget

    # regex_pattern = '^https:\/\/www\.youtube\.com\/watch\?v='
    regex_pattern = r'^https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+$'
    
    if re.match(regex_pattern, link):
        # print("Downloading...")
        status_label.configure(text="Downloading...", text_color="orange")
        try:
            # ytObject = YouTube(link, on_progress_callback=on_progress)
            # Erorr: startDownload.<locals>.<lambda>() takes 0 positional arguments but 3 were given
            # ytObject = YouTube(link, on_progress_callback=lambda: on_progress(pPercentage)) # Errors on_progress_callback=on_progress
            ytObject = YouTube(link, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining, pPercentage, progressBar),
                               on_complete_callback=lambda stream, file_path: on_complete(stream, file_path, pPercentage, progressBar))

            video = ytObject.streams.get_highest_resolution()
            video_title = video.title
            download_path = get_downloads_directory()
            if os.path.exists(download_path + '/' + video_title + '.mp4'):
                status_label.configure(text=f"The video already exists! /is Downloaded/", text_color="red")
                return 
        
            video.download(output_path=download_path, filename=f"{video_title}.mp4")

            status_label.configure(text=f"Download of '{video_title}' has completed.", text_color="green")
        except Exception as e:
            # pass 
            print("Erorr: {}".format(e))
            status_label.configure(text=f"Download of '{video.title}' failed.", text_color="red")
    else:
        # tkinter.messagebox.showerror("Invalid Link", "Please enter a valid YouTube link.")
        status_label.configure(text="Invalid Link, please enter a valid YouTube link", text_color="red")

def calculate_center_position(app, window_width, window_height):
    # Get the screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calculate the x and y coordinates for the Tk root window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    return f"{window_width}x{window_height}+{x}+{y}"

def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    # app.geometry("720x480")

    # Set the window size
    window_width = 600 # 720
    window_height = 360 # 480

    # Set the initial position and size of the window
    app.geometry(calculate_center_position(app, window_width, window_height))

    app.title("Youtube video downloader")

    # Add UI Elements
    title = customtkinter.CTkLabel(app, text="") # Insert a youtube link
    title.pack(padx=10, pady=10)

    # Link input
    default_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


    link_entry = customtkinter.CTkEntry(app, width=350, height=40)
    link_entry.insert(0, default_link)  # Set the initial value
    link_entry.pack()

    # Download button
    download = customtkinter.CTkButton(app, text="Download", command=lambda: startDownload(link_entry, status_label, pPercentage, progressBar))
    download.pack(pady=10)

    # Add a label to show the status
    status_label = customtkinter.CTkLabel(app, text="Type in an youtube link")
    status_label.pack(pady=10)

    # Progress percentage 
    pPercentage = customtkinter.CTkLabel(app, text="0%")
    pPercentage.pack(pady=10)
    progressBar = customtkinter.CTkProgressBar(app, width=400)
    progressBar.set(0)
    progressBar.pack(padx=10, pady=10)

    author_label = customtkinter.CTkLabel(app, height=6, text="created by Vladimir Balabanov")
    author_label.pack(padx=40, pady=40)

    # Run app
    app.mainloop()

if __name__ == "__main__":
    main()
    # downloads_dir = get_downloads_directory()
    # print(f"Downloads directory: {downloads_dir}")
# if __name__ == "__main__":