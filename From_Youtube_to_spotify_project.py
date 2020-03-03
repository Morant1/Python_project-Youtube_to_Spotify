import json
import requests
from youtube_dl import YoutubeDL
import spotipy.util as util
import spotipy

#For authorization:
"""
username = ''
client_id = ''
client_secret = ''
redirect_uri = 'http://localhost:8888/callback/'
scope = 'playlist-modify-private'

def init_spotify_client():
        print('Initialising Spotify Client....')
        token = util.prompt_for_user_token(username, scope,
                                           client_id=client_id,
                                           client_secret=client_secret,
                                           redirect_uri=redirect_uri)

init_spotify_client()
"""



def check_url(youtube_url):  # Youtube URL contains 11 unique channel ID
    try:
        if "v" in youtube_url:
            ind = youtube_url.find("v")
            structure = youtube_url[0:ind + 2]
            channel_ID = youtube_url[ind + 2:]
            if structure != "https://www.youtube.com/watch?v=" or len(channel_ID) != 11:
                print("***Check your URL***")
                raise ArgumentError(youtube_url)
            else:
                print("Nice song!")
        else:
            print("***Check your URL***")
            raise ArgumentError(youtube_url)

    except ArgumentError as e:
        print(e)
        main()


class ArgumentError(Exception):
    def __init__(self,arg):
        self._arg = arg
    def __str__(self):
        return 'Please insert a valid Youtube URL structure ''http://www.youtube.com/watch?v=XXXXXXXXXX''.\nCheck your input %s and try again\n'  % self._arg

class From_Youtube_to_spotipy:
    def __init__(self,youtube_url,token,username,playlist_name):
        self.youtube_url = youtube_url
        self.token = token
        self.username = username
        self.playlist_name= playlist_name

    def info(self):
           # Using youtube_dl to collect the song name & artist name
           video = YoutubeDL().extract_info(self.youtube_url, download=False)
           song_name = video["track"]
           artist = video["artist"]
           song_info = [song_name,artist]
           return song_info

    def create_playlist(self):
           #Creating A New Spotify playlist
            request_body = json.dumps({
                  "name": "{}".format(self.playlist_name),
                  "description": "From URL to a spotify song",
                  "public": False})

            query = "https://api.spotify.com/v1/users/{}/playlists".format(self.username)
            response = requests.post(
                   query,
                   data=request_body,
                   headers={
                    "Content-Type": "application/json",
                     "Authorization": "Bearer {}".format(self.token)
                    })
            response_json = response.json()
            playlist_id = response_json["id"]
            return playlist_id #Getting the playlist ID


    def search_song(self):
          #let's search for the song
          list_info = self.info()
          query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
                list_info[0],
                list_info[1]
          )

          response = requests.get(
                query,
                headers={
                    "Content-Type": "application/json",
                     "Authorization": "Bearer {}".format(self.token)
                      })
          response_json = response.json()
          song = response_json['tracks']['items']
          uri = song[0]["uri"]
          uris = [uri]
          return uris #Getting the song Spotify uri


    def add_song_to_playlist(self):

          request_data = json.dumps(self.search_song())
          query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.create_playlist())
          response = requests.post(
                query,
                data=request_data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                })
          response_json = response.json()
          return response_json #On success, the response body will contains a 'snapshot_id' in JSON format and the HTTP status code 200.


def main():
          #You can take this URL for example - https://www.youtube.com/watch?v=Mrfu0FBB110
          your_youtube_url = input("Please insert your Youtube music video URL with one space at last:") #a space is required for known bug/feature in pycharm
          youtube_url =  your_youtube_url.strip()
          check_url(youtube_url)
          token = input("Please insert your Token:")
          username = input("Please insert your Username:")
          playlist_name = input("How would you like to call your new playlist on Spotify?")
          personal_info = [youtube_url,token,username,playlist_name] #list of personal_info


          my_spotify = From_Youtube_to_spotipy(personal_info[0],personal_info[1],personal_info[2],personal_info[3])
          my_spotify.add_song_to_playlist()
main()

