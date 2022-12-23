import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://petemango:ay4h7vRoWNv6BD1a@spotify-tracker-cluster.jbudfme.mongodb.net/?retryWrites=true&w=majority")
db = cluster["spotify_tracker_data"]
collection = db["songs_listened"]

def post_to_cloud (song_info):
    name = song_info.name
    artist = song_info.artist
    id = song_info.id
    link = song_info.link

    post = {"name": name, "artist": artist, "identifier": id, "link": link}
    collection.insert_one(post)

