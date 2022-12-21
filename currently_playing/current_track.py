import time
import requests
import pprint 
spotify_access_token = 'BQCb54AuyZ_EcSQPIfSVgZMJKsG2w2yd-iKYHXh6o5Qn3u1by0iVrknVYGIgrB-Y6BVm7sj2Jr70vLNa4aH-roCqHdbdUGR4db-c-1fK74Bt1yzqASUrAU_AJNuZkm_ZOJ584uFITtRSOP1Flbg4xuthRqrGtf2T-LsFKTd2o_2QbufRfwF2QVA'
spotify_get_current_track_url = 'https://api.spotify.com/v1/me/player/currently-playing'

# class for complete song info
class song_info:
    def __init__(current_song, name, artist, id, link):
        current_song.name = name
        current_song.artist = artist
        current_song.id = id
        current_song.link = link

# class for reduced song info
class reduced_song_info:
    def __init__(current_song, name, artist):
        current_song.name = name
        current_song.artist = artist

# gets the current track using the spotify authorization token
def get_current_track (access_token):
    response = requests.get(
        spotify_get_current_track_url,
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
    )
    response_json = response.json()

    # single variable (ex. only one name, one id and one spotify link)
    track_id = response_json['item']['id']
    track_name = response_json['item']['name']
    link = response_json['item']['external_urls']['spotify']

    # multi variable (ex. certain songs can have multiple artists)
    artists = [artist for artist in response_json['item']['artists']]
    artists_name = ', '.join([artist['name'] for artist in artists])

    # return all the data in a single variable
    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_name,
        "link": link
    }

    return current_track_info

# print the full song data
def print_full_data (song_info):
    with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/currently_playing/full_data.txt", "at") as file:
        file.write(song_info.name + "\n")
        file.write(song_info.artist + "\n")
        file.write(song_info.id + "\n")
        file.write(song_info.link + "\n")
        file.write("\n")
    file.close()

# print the simplified song data
def print_limited_data (reduced_song_info):
    with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/currently_playing/reduced_song_info.txt", "at") as file:
        file.write(reduced_song_info.name + "\n")
        file.write(reduced_song_info.artist + "\n")
        file.write("\n")
    file.close()

# main function to process the data pulled from the API
def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(spotify_access_token)
        
        if current_track_info['id'] != current_track_id:
            # current_song = song_info(current_track_info.get("name"), current_track_info.get("artists"), 
            # current_track_info.get("id"), current_track_info.get("link"))

            red_song_info = reduced_song_info(current_track_info.get("name"), current_track_info.get("artists"))
            ful_song_info = song_info(current_track_info.get("name"), current_track_info.get("artists"), current_track_info.get("id"), current_track_info.get("link"))

            print_full_data(ful_song_info)
            print_limited_data(red_song_info)

            # output_string = pprint.pformat(current_track_info, indent=4)
            # print_string = output_string + "\n"
            # # print(output_string)
            # with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/currently_playing/recently_played_tracks.txt", "at") as file:
            #     file.write(print_string)
            #     file.close()
            # pprint(current_track_info, indent=4)
            current_track_id = current_track_info['id']
    time.sleep(1)

if __name__ == '__main__':
    main()