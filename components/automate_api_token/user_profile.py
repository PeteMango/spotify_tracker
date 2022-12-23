import requests
from automated_api import *

response = requests.get(
    spotify_user_url,
    headers = {
        "Authorization": f"Bearer {token}"
    }
)

response_json = response.json()
pprint(response_json, indent=4)
