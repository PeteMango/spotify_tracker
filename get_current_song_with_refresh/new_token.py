import requests
import json
from secret import *


class refresh:
    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64_message

    def refresh(self):
        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refresh_token},
                                 headers={"Authorization": "Basic " + base_64_message})

        response_json = response.json()
        print(response_json)

        return response_json["access_token"]


a = refresh()
new_access_token = a.refresh()
# a.refresh()
