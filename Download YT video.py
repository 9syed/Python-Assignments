from pytube import YouTube

yt_link = "https://www.youtube.com/watch?v=0blV4zbXYbQ"
youtube = YouTube(yt_link)
youtube.streams.first().download()