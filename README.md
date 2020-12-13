# SpotifySongD
Downloads your spotify liked playlist from youtube based on the songs names. Some songs may not be able to be found or may be named improperly after downloading.
Run with the command ```python run.py spotify_username download_location threads```
## Requirments 
- Python 3.4 + 
- [youtube-dl](https://pypi.org/project/youtube_dl/)
- [youtube-search](https://pypi.org/project/youtube-search/)
- [spotipy](https://pypi.org/project/spotipy/)

The enviorment variables SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI must be set. Refer to the [spotipy](https://spotipy.readthedocs.io/en/2.16.1/)
documentation for a guide how to do this.
