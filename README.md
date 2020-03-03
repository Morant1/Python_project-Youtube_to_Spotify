## Python_project-YoutubetoSpotify-
Enter a Youtube music video URL  link and find the song on your spotify in a new playlist!

**Prior requirements**:
1. Install All Dependencies - 
```
json
requests
youtube_dl
spotipy
```

#you can read the Authorization Guide of spotify [here](https://developer.spotify.com/documentation/general/guides/authorization-guide/)

2. Please follow my steps to get permission to access the Spotify API:
(in general, we need to create an app that will access the Spotify API once it gets permission from the user)

- [x]  log in and register a Spotify app [here](https://developer.spotify.com/dashboard/login)
- [x] Go to your new developer dashboard and click on "Create an App" (write the details as you desire).
- [x] Go to 'Edit settings', insert and save to following Redirect URI:'http://localhost:8888/callback/'
- [x] Save your Client Secret and Client ID (you'll find them in the app panel).
- [x] Collect your Username by Log into Spotify and then go here: [Account Overview](https://www.spotify.com/us/account/overview/) and its your Username.
![alt text](username.png)
- [x] Run the authurization part in the code with the variables you just collected.
```
username = 'insert here'
client_id = 'insert here'
client_secret = 'insert here'
redirect_uri = 'http://localhost:8888/callback/'
scope = 'playlist-modify-private'

def init_spotify_client():
        print('Initialising Spotify Client....')
        token = util.prompt_for_user_token(username, scope,
                                           client_id=client_id,
                                           client_secret=client_secret,
                                           redirect_uri=redirect_uri)

```
        
- [x] Once you run the code,it will open an authorization panel in your web browser. Follow the link,log in and click on **agree** to authorize your app.
- [x] Copy the URI in your console as required - the next step will take you to redirect URI which may be a nonexistent page (so don't worry...)
- [x] Get your token [here](https://developer.spotify.com/console/post-playlist-tracks/?playlist_id=&position=&uris=):
Click 'get token' and then select your scopes : "playlist-modify-private" and "playlist-read-private" and  request the token.

- [x] **it's a wrap! you have everything you need to run the code.**


## final result on my app: 
#### Hebrew version
![alt text](Finalresult.jpg)




