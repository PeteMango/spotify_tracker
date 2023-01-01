import base64
client_id = 'a2eac0acaaa34f6ab11095c0eac75662'
client_secret = 'b0038a3ad4da47fdad2efcb4e608132d'
refresh_token = 'AQCkq9H7LLP-kzUI9SUV9M0RqfLid9tv9W_9kA_KEERV_OjJfPiRLS5vjxDCiH90So7P3cDpA2mY4KMAxX6gKSGvSizSWPNyhmMDStoKaudf0tbuIww86adasuhdBF6I4ac'
spotify_user_name = "PeteMango"

# combining client_id and client_secret + base 64 encoding
# a2eac0acaaa34f6ab11095c0eac75662:b0038a3ad4da47fdad2efcb4e608132d
# YTJlYWMwYWNhYWEzNGY2YWIxMTA5NWMwZWFjNzU2NjI6YjAwMzhhM2FkNGRhNDdmZGFkMmVmY2I0ZTYwODEzMmQ=

# curl command:
# curl -H "Authorization: Basic YTJlYWMwYWNhYWEzNGY2YWIxMTA5NWMwZWFjNzU2NjI6YjAwMzhhM2FkNGRhNDdmZGFkMmVmY2I0ZTYwODEzMmQ=" -d grant_type=authorization_code -d code=AQCQTJTrW1v100UPLvQTZF_odR36QpUKB50OX-LwBZpOj4w18qaUGYQUIqYRrw6SM-OqUpjZ-2hXow3pmuHevikSRYeq-0F1RycP-qjHh1HEC23tZkmypzcZdRCULxkprX-zlEk4EYqeiEp8Y0bt2rOQWn4z5vIuqzjKngT6Of-CPSWwN1d3lVxfmIWfOMy70UzvcBOjoduUbTV33w -d redirect_uri=https%3A%2F%2Fgithub.com%2FPeteMango https://accounts.spotify.com/api/token

# authorization link:
# https://accounts.spotify.com/authorize?client_id=a2eac0acaaa34f6ab11095c0eac75662&response_type=code&redirect_uri=https%3A%2F%2Fgithub.com%2FPeteMango&scope=user-read-currently-playing

message = f"{client_id}:{client_secret}"
message_bytes = message.encode('ascii')
base_64_bytes = base64.b64encode(message_bytes)
base_64_message = base_64_bytes.decode('ascii')
