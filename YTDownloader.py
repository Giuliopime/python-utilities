import re
from pytube import YouTube, Playlist
from tkinter import filedialog
from tkinter import *


root = Tk()
root.withdraw()
print("Select the folder where you would like to download your stuff")
FOLDER = filedialog.askdirectory()

YOUTUBE_STREAM_AUDIO = '140'
choice = ""
while choice != "0":
    choice = input("\nReply with one of the following numbers to choose the operation to perform:"
                   "\n0 - Terminate the process"
                   "\n1 - Download a YouTube video"
                   "\n2 - Download a YouTube Playlist\n")

    if choice == "0":
        exit(0)

    elif choice == "1":
        video = YouTube(input("\nPlease input the YouTube video link\n"))

        dlType = ""
        while dlType != "1" and dlType != "2":
            dlType = input(
                "\nInsert:\n- '1' to download only audio\n- '2' to download the full video\n")

        streams = video.streams

        print("\nDownloading...")

        if dlType == "1":
            audioStream = streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
            audioStream.download(output_path=FOLDER)
        else:
            streams[0].download(output_path=FOLDER)

        print("Downloaded " + video.title)

        print("\nSuccessfully downloaded YouTube video: " + video.title)

    elif choice == "2":
        playlist = Playlist(input("\nPlease input the YouTube playlist link\n"))

        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")  # Fixes empty playlist

        dlType = ""
        while dlType != "1" and dlType != "2":
            dlType = input(
                "\nInsert\n- '1' to download only audio\n- '2' to download the full video\n")

        print("\nDownloading...")

        if dlType == "1":
            for video in playlist.videos:
                audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
                audioStream.download(output_path=FOLDER)
                print("Downloaded " + audioStream.title)
        else:
            for video in playlist.videos:
                video.streams[0].download(output_path=FOLDER)
                print("Downloaded " + video.title)

        print("\nSuccessfully downloaded YouTube playlist: " + playlist.title)

