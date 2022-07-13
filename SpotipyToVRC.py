import spotipy
import socket
from spotipy.oauth2 import SpotifyOAuth

#getting spotify music data
SPOTIPY_CLIENT_ID='CLIENT ID'
SPOTIPY_CLIENT_SECRET='CLIENT SECRET'
SPOTIPY_REDIRECT_URI='http://localhost'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID,
                                               SPOTIPY_CLIENT_SECRET,
                                               SPOTIPY_REDIRECT_URI))

data = sp.current_user_playing_track()
print(data['item']['name']+' - '+data['item']['artists'][0]['name'])


#sending data part
import socket

UDP_IP = "localhost"
UDP_PORT = 9000
MESSAGE = "/text/data/" + data
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
