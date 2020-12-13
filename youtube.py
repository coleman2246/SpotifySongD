from youtube_search import YoutubeSearch
import youtube_dl

def get_video(term):
    results = YoutubeSearch(term, max_results=1).to_dict()
    url = None
    try:
        url = "https://www.youtube.com/"+results[0]["url_suffix"]
    except:
        print("Couldnt Find :",term)
    return url


def download_list(song_urls,dir):
    ydl_opts = {'ignoreerrors': True, 
                'format': 'bestaudio/best',
                "postprocessors": [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'}],
                'outtmpl': dir+'/%(title)s.%(ext)s',
                }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(song_urls)

