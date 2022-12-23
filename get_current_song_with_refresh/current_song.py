import time
import pprint 
import requests
from new_token import *

current_track_url = 'https://api.spotify.com/v1/me/player/currently-playing'
access_token = new_access_token

class song_info:
    def __init__(current_song, name, artist, id, link):
        current_song.name = name
        current_song.artist = artist
        current_song.id = id
        current_song.link = link

class reduced_song_info:
    def __init__(current_song, name, artist):
        current_song.name = name
        current_song.artist = artist

def print_full_data (song_info):
    with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/get_current_song_with_refresh/full_song_info.txt", "at") as file:
        file.write(song_info.name + "\n")
        file.write(song_info.artist + "\n")
        file.write(song_info.id + "\n")
        file.write(song_info.link + "\n")
        file.write("\n")
    file.close()

def print_limited_data (reduced_song_info):
    with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/get_current_song_with_refresh/reduced_song_info.txt", "at") as file:
        file.write(reduced_song_info.name + "\n")
        file.write(reduced_song_info.artist + "\n")
        file.write("\n")
    file.close()

def get_current_song (access_token):
    response = requests.get(
        current_track_url,
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
    )

    response_json = response.json()
    # print(response_json)

    track_id = response_json['item']['id']
    track_name = response_json['item']['name']
    link = response_json['item']['external_urls']['spotify']
    artists = [artist for artist in response_json['item']['artists']]
    artists_name = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_name,
        "link": link
    }

    return current_track_info

def main():
    current_track_id = None
    while True:
        current_track_info = get_current_song(access_token)
        
        if current_track_info['id'] != current_track_id:
            red_song_info = reduced_song_info(current_track_info.get("name"), current_track_info.get("artists"))
            ful_song_info = song_info(current_track_info.get("name"), current_track_info.get("artists"), current_track_info.get("id"), current_track_info.get("link"))

            print_full_data(ful_song_info)
            print_limited_data(red_song_info)

            current_track_id = current_track_info['id']
    time.sleep(10)

if __name__ == '__main__':
    main()