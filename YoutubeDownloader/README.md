
# YouTube Downloader

## Overview
**YouTube Downloader** is a simple Python application built with the [pytube](https://github.com/pytube/pytube) library and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) framework. It allows users to download [YouTube](https://youtube.com) videos by providing a video link.

## Demo

![Youtube Downloader Demo](Youtube%20Downloader%20Demo.gif)

 
## Features
- Download YouTube videos in high resolution.
- Track download progress with a percentage indicator and a progress bar.
- Visual cues for download status.
- User-friendly interface created using CustomTkinter.

## Requirements
- [pytube](https://github.com/pytube/pytube): A lightweight, dependency-free Python library for downloading YouTube videos.
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): A custom-themed Tkinter library to enhance GUI aesthetics.
- Python 3.x: Make sure you have a Python 3.x interpreter installed on your system.

Install the required Python packages like so:
```batch
pip install git+https://github.com/pytube/pytube
pip install customtkinter
```

## Usage
1. Launch the application.
2. Paste a valid YouTube video link into the provided entry field.
3. Click the "Download" button to initiate the download.
4. Track the download progress through the displayed percentage and progress bar.
5. Once the download is complete, the application will notify you.


## Notes
- The default download location is the system's Downloads directory.
- Ensure the provided YouTube link is valid before initiating the download.

## Contributors
Vladimir Balabanov ( **Grrr1337** )

## License
This project is licensed under the MIT License