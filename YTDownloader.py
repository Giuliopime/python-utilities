from pytube import YouTube

ytd = YouTube(input("Please input the yt link\n"))

dlType = ""
while dlType != "audio" and dlType != "video":
    dlType = input("Insert\n- 'audio' to download only audio\n- 'video' to download the full video\n").lower()

stream = ytd.streams.filter(only_audio=(True if dlType == "audio" else False))

print("Downloading...")

stream[0].download(".")

print("Successfully downloaded audio from the provided link")
