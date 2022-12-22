from pytube import YouTube
link = input('Link: ')
yt = YouTube(link)
print(f'Name: {yt.title}\nViews: {yt.views}')

# download highest resolution
# yt.streams.get_highest_resolution().download()

# download desired resolution
yt.streams.filter(res = '360p').first().download()