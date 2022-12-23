import pymongo
from pymongo import MongoClient

# username: petemango
# password: ay4h7vRoWNv6BD1a

# mongodb+srv://petemango:<password>@spotify-tracker-cluster.jbudfme.mongodb.net/?retryWrites=true&w=majority

cluster = MongoClient("mongodb+srv://petemango:ay4h7vRoWNv6BD1a@spotify-tracker-cluster.jbudfme.mongodb.net/?retryWrites=true&w=majority")
db = cluster["spotify_tracker_data"]
collection = db["songs_listened"]

# post = {"_id": 0, "name": "tim", "score": 5}
# collection.insert_one(post)

# post2 = {"_id": 1, "name": "peter", "score": 10}
# post3 = {"_id": 2, "name": "norman", "score": 7}
# collection.insert_many([post2, post3])

find_result = collection.find({})
# print(find_result)

for result in find_result:
    print(result)