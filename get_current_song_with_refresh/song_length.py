import time
import pprint 
import requests
from new_token import *

current_track_url = 'https://api.spotify.com/v1/me/player/currently-playing'
access_token = new_access_token

class song_length:
    def __init__(current_song, duration):
        current_song.duration = duration

def get_song_length(access_token):
    response = requests.get(
        current_track_url,
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
    )
    response_json = response.json()
    time_seconds = response_json['item']['duration_ms'] / 1000

    minutes = (int)(time_seconds / 60)
    seconds = (int)(time_seconds - 60 * minutes)
    current_track_length = {
        "minutes": minutes,
        "seconds": seconds
    }
    return current_track_length

