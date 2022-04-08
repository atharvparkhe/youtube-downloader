import ssl
from pytube import YouTube, Playlist
ssl._create_default_https_context = ssl._create_unverified_context


video_link = "https://youtu.be/TP1xs1hF2ZE"
playlist_link = "https://youtube.com/playlist?list=PLgzgA64MLAfljRZTbPfOgBtJMBBxC0LP2"

################################################################

yt = YouTube(video_link)

print(yt.title)
print(yt.description)
print(yt.thumbnail_url)

videos = yt.streams.all()
videos = yt.streams.filter(only_audio = True)
videos = yt.streams.filter(only_video = True) 

vid = list(enumerate(videos))

for i in vid:
    print(i)

videos[4].download()
print("Successfully Downloaded")

################################################################


pl = Playlist(playlist_link)

print(pl.title)

for i in pl.videos:
    i.streams.first().download()

print("Successfully Downloaded")


################################################################