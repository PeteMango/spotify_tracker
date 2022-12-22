import base64
import requests
from pprint import pprint
from secret import *

auth_url = 'https://accounts.spotify.com/api/token'
spotify_get_current_track_url = 'https://api.spotify.com/v1/me/player/currently-playing'

auth_header = {}
auth_data = {}

message = f"{client_id}:{client_secret}"
message_bytes = message.encode('ascii')
base_64_bytes = base64.b64encode(message_bytes)
base_64_message = base_64_bytes.decode('ascii')

# print(base_64_message)

auth_header['Authorization'] = f"Basic {base_64_message}"
auth_data['grant_type'] = "client_credentials"

res = requests.post(auth_url, headers=auth_header, data=auth_data)
token = res.json()['access_token']
print(res.json())
print(token)


