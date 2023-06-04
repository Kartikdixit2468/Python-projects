from pytube import Playlist

URL_PLAYLIST = input("Paste your playlist link here")

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)

print(urls)
try:
    with open("playlist_url.txt", "w") as file:
        try:
            for url in urls:
                file.write(f"{url}\n ")
            print("Task Completed | Links saved to -  playlist_url.txt")
        except Exception as e:
            print(f"An Error occured while writing links to file | Error -: /n{e}")

except Exception as e:
    print(f"Task coud not be completed an error occured | Error -: /n{e}")


print("Exitting")