from pytube import YouTube

yt_link = "https://www.youtube.com/watch?v=Ql9-mK6cilQ"
youtube = YouTube(yt_link)
youtube.streams.first().download()