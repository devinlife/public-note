from pytube import YouTube

VIDEO_URL = 'https://www.youtube.com/watch?v=I845O57ZSy4'  # 'VIDEO_ID'를 실제 비디오의 ID로 바꿔주세요.

yt = YouTube(VIDEO_URL)
print("Title:", yt.title)
print("Description:", yt.description)
print("Views:", yt.views)
print("Rating:", yt.rating)
print("Rating:", yt.caption_tracks)
print("Rating:", yt.captions)
print(dir(yt))
