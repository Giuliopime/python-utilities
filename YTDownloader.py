from pytube import YouTube, Playlist
from moviepy.editor import *
from tkinter import filedialog
from tkinter import *


root = Tk()
root.withdraw()
print("Select the folder where you would like to download your stuff")
FOLDER = filedialog.askdirectory()

YOUTUBE_STREAM_AUDIO = '140'
choice = ""
while choice != "0":
    try:
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

            path = streams[0].download(output_path = FOLDER)

            if dlType == "1":
                videoFile = VideoFileClip(path)
                videoFile.audio.write_audiofile(FOLDER + "/" + video.title + ".mp3")
                videoFile.close()
                os.remove(path)

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

            for video in playlist.videos:
                path = video.streams[0].download(output_path=FOLDER)
                if dlType == "1":
                    videoFile = VideoFileClip(path)
                    videoFile.audio.write_audiofile(FOLDER + "/" + video.title + ".mp3")
                    videoFile.close()
                    os.remove(path)

                print("Downloaded " + video.title)

            print("\nSuccessfully downloaded YouTube playlist: " + playlist.title)

    except Exception:
        print("You didn't provide a correct link")
