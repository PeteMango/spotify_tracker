import time as t
import pprint
import requests
from datetime import *
from new_token import *
from song_length import *
from handle_backend import *

current_track_url = 'https://api.spotify.com/v1/me/player/currently-playing'
access_token = new_access_token
change_day = False


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


def print_full_data(song_info):
    with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/tracked_data/full_song_info.txt", "at") as file:
        file.write(song_info.name + "\n")
        file.write(song_info.artist + "\n")
        file.write(song_info.id + "\n")
        file.write(song_info.link + "\n")
        file.write("\n")
    file.close()


def print_limited_data(reduced_song_info):
    with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/tracked_data/reduced_song_info.txt", "at") as file:
        file.write(reduced_song_info.name + "\n")
        file.write(reduced_song_info.artist + "\n")
        file.write("\n")
    file.close()


def get_current_song(access_token):
    response = requests.get(
        current_track_url,
        headers={
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


def get_current_listening_time():
    f = open(
        "/Users/petemango/SIDE PROJECTS/spotify_tracker/tracked_data/listen_time.txt", "r")
    current_time = int(f.readline())
    return current_time


def update_listening_time(current_time, song_length):
    f = open(
        "/Users/petemango/SIDE PROJECTS/spotify_tracker/tracked_data/listen_time.txt", "w")
    updated_time = current_time + song_length
    f.write(str(updated_time))
    f.close()


def weekly_tracking(time_listened):
    f = open(
        "/Users/petemango/SIDE PROJECTS/spotify_tracker/tracked_data/weekly_result.txt", "a")
    f.writelines(time_listened)
    f.write("\n")


def reset_counter():
    f = open(
        "/Users/petemango/SIDE PROJECTS/spotify_tracker/tracked_data/listen_time.txt", "r")
    total_listening_time = int(f.readline())
    weekly_tracking(total_listening_time)
    f.close()

    f = open(
        "/Users/petemango/SIDE PROJECTS/spotify_tracker/tracked_data/listen_time.txt", "w")


def main():
    current_track_id = None
    while True:
        current_date = datetime.now()
        day_of_week = current_date.weekday()
        # print(current_date)
        # print(day_of_week)
        current_track_info = get_current_song(access_token)

        if day_of_week == 1:
            change_day = True

        if day_of_week == 0 and change_day == False:
            reset_counter()

        if current_track_info['id'] != current_track_id:
            red_song_info = reduced_song_info(current_track_info.get(
                "name"), current_track_info.get("artists"))
            ful_song_info = song_info(current_track_info.get("name"), current_track_info.get(
                "artists"), current_track_info.get("id"), current_track_info.get("link"))

            print_full_data(ful_song_info)
            print_limited_data(red_song_info)

            post_to_cloud(ful_song_info)
            remove_duplicate()

            current_song_length = get_song_length(access_token)
            song_seconds = current_song_length['minutes'] * \
                60 + current_song_length['seconds']
            update_listening_time(get_current_listening_time(), song_seconds)

            time_listened = get_current_listening_time() + song_seconds
            post_listening_time(time_listened)

            current_track_id = current_track_info['id']
        t.sleep(20)


if __name__ == '__main__':
    main()
