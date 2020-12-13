import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_search import YoutubeSearch
import youtube
import numpy as np
import threading

if len(sys.argv) > 3:
    username = sys.argv[1]
    direc = sys.argv[2]
    thread_count = int(sys.argv[3])

else:
    print("usage: python run.py <username> <directory> <threadcount>")
    sys.exit()

scope = 'user-library-read'
token = util.prompt_for_user_token(username,scope)
songs_names = [] 


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    while results:
        for item in results['items']:
            track = item['track']
            print(str(track['name'] + ' - ' + track['artists'][0]['name']))
            songs_names.append(str(track['name'] + ' - ' + track['artists'][0]['name']))
        if results["next"]:
            results = sp.next(results)
        else:
            results = None


def partition_list(list,n):
    return np.array_split(list,n)

def find_song(songs,direc):
    temp = []
    for count,i in enumerate(songs):
        print(count, "/", len(songs))
        url = youtube.get_video(i)
        if url != None:
            temp.append(url)
    print("Startin Downloading")
    youtube.download_list(temp,direc)

cut_up = partition_list(songs_names,thread_count)
threads = []

for i in range(thread_count):
    print(cut_up[i])
    t = threading.Thread(target=find_song, args=(cut_up[i],direc,))
    threads.append(t)
    print(i)
    t.start()

for i in threads:
    i.join()


