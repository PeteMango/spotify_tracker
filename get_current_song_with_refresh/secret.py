import base64
client_id = 
client_secret = 
refresh_token = 
spotify_user_name = "PeteMango"

message = f"{client_id}:{client_secret}"
message_bytes = message.encode('ascii')
base_64_bytes = base64.b64encode(message_bytes)
base_64_message = base_64_bytes.decode('ascii')
