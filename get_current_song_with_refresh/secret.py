import base64
client_id = 'a2eac0acaaa34f6ab11095c0eac75662'
client_secret = 'b0038a3ad4da47fdad2efcb4e608132d'
refresh_token = 'AQCkq9H7LLP-kzUI9SUV9M0RqfLid9tv9W_9kA_KEERV_OjJfPiRLS5vjxDCiH90So7P3cDpA2mY4KMAxX6gKSGvSizSWPNyhmMDStoKaudf0tbuIww86adasuhdBF6I4ac'
spotify_user_name = "PeteMango"

message = f"{client_id}:{client_secret}"
message_bytes = message.encode('ascii')
base_64_bytes = base64.b64encode(message_bytes)
base_64_message = base_64_bytes.decode('ascii')
