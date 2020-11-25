import os
import time
from pytube import YouTube
from moviepy.editor import *

ytd = YouTube(input("Please input the yt link\n"))

dlType = ""
while dlType != "audio" and dlType != "video" and dlType != "1" and dlType != "2":
    dlType = input("Insert\n- 'audio' or '1' to download only audio\n- 'video' or '2' to download the full video\n").lower()

stream = ytd.streams

print("Downloading...")

if dlType == "audio" or dlType == "1":
    filePath = stream[0].download(".")
    video = VideoFileClip(filePath)
    video.audio.write_audiofile("./" + ytd.title + ".mp3")
    video.close()
    os.remove(filePath)


print("Successfully downloaded yt video")
