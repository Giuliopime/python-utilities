# import os
from pytube import YouTube
# from moviepy.editor import *

ytd = YouTube(input("Please input the yt link\n"))

dlType = ""
while dlType != "audio" and dlType != "video":
    dlType = input("Insert\n- 'audio' to download only audio\n- 'video' to download the full video\n").lower()

stream = ytd.streams.filter(only_audio=(True if dlType == "audio" else False))

print("Downloading...")

filePath = stream[0].download(".")

"""
if dlType == "audio":
    video = VideoFileClip(filePath)
    video.audio.write_audiofile("./", ytd.title)
    os.remove(filePath)
"""

print("Successfully downloaded yt video")
