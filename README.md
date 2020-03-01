## Python_project-YoutubetoSpotify-
Enter a Youtube music video URL  link and find the song on your spotify in a new playlist!

##**prior requirements**:
A. Install All Dependencies - 
```
json
requests
youtube_dl
spotipy.util
spotipy
```

#you can read the Authorization Guide of spotify [here](https://developer.spotify.com/documentation/general/guides/authorization-guide/)

- [ ] Please follow my steps to get permission to access the Spotify API:
(in general, we need to create an app that will access the Spotify API once it gets permission from the user)

1. log in and register a Spotify app [here](https://developer.spotify.com/dashboard/login)
2.Go to your new developer dashboard and just click on "Create an App" (don't worry about the details).
3.Save your Client Secret and Client ID (you'll find them in the app panel).
4.Collect your Username by Log into Spotify and then go here: [Account Overview](https://www.spotify.com/us/account/overview/) and its your Username.
5.run the authurization part in the code with the variables you just collected.
6.Once your run the code,it will open an authorization panle in your web browser. Follow the link,log in  and you should see somthing like this:

Please click on agree to authorize your app
7.the next step will take your to redirect URI whitch may be a nonexistent page.
8.Get your token [here](https://developer.spotify.com/console/post-playlist-tracks/?playlist_id=&position=&uris=):
Click 'get token' and then select your scopes : "playlist-modify-private" and "playlist-read-private" and  request the token

9.**it's a wrap! you have everything you need to run the code.**




