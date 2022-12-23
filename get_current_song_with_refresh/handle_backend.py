import pymongo
from datetime import *
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://petemango:ay4h7vRoWNv6BD1a@spotify-tracker-cluster.jbudfme.mongodb.net/?retryWrites=true&w=majority")
db = cluster["spotify_tracker_data"]
collection = db["songs_listened"]
listen = db["listening_time"]

def post_to_cloud (song_info):
    name = song_info.name
    artist = song_info.artist
    id = song_info.id
    link = song_info.link

    post = {"name": name, "artist": artist, "identifier": id, "link": link}
    collection.insert_one(post)

def remove_duplicate ():
    search_result = collection.find({})
    for result in search_result:
        name = result["name"]
        search_name = collection.find({"name":name})
        
        temp_value = search_name[0]
        collection.delete_many({"name":name})
        collection.insert_one(temp_value)

        # print(temp_value)

def post_listening_time (total_listening_time):
    current_date = datetime.now()
    minutes = int(total_listening_time / 60)
    seconds = int(total_listening_time % 60)
    post = {"date-time": current_date, "minutes":minutes, "seconds":seconds}
    listen.insert_one(post)