import time
import requests
import pprint 
spotify_access_token = 'BQBnMJNL_uZcz17VJa5zaIi43U94J_ZTaaZSjGzBiZuWKtUgI9YPAphlwmS7OMJyduYneVQzC36X_IvL3U1biixlG1X1El4QEF_8w0AIEV_vJ2C2J9soKIzMhDa0SnSNWnUX7FjtKIuvhP2zBgqJEQNnSN04FUnJ1m5nsK02BoDdMeRWLJ1xTsw'
spotify_get_current_track_url = 'https://api.spotify.com/v1/me/player/currently-playing'

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

class song_info:
    def __init__(current_song, name, artist, id, link):
        current_song.name = name
        current_song.artist = artist
        current_song.id = id
        current_song.link = link

def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(spotify_access_token)
        
        if current_track_info['id'] != current_track_id:
            # current_song = song_info(current_track_info)

            output_string = pprint.pformat(current_track_info, indent=4)
            print_string = output_string + "\n"
            # print(output_string)
            with open("/Users/petemango/SIDE PROJECTS/spotify_tracker/recently_played_tracks.txt", "at") as file:
                file.write(print_string)
                file.close()
            # pprint(current_track_info, indent=4)
            current_track_id = current_track_info['id']
    time.sleep(1)

if __name__ == '__main__':
    main()