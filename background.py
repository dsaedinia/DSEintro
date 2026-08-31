import spotipy
import json
import os
from PIL import Image
from urllib.request import urlopen
from spotipy.oauth2 import SpotifyClientCredentials

# from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

##################################
# Name: Daniel (Danny) Saedi Nia #
##################################

# Fun fact: ...

# load env variables --> spotify API keys
load_dotenv()

# Get the list dict of top artists and their IDs
# See comment way down below for how I got these if interested!
with open("top_artists.json", "r") as f:
    top_artists = json.load(f)

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

print("Danny's Top 10 Artists on Spotify:")
idx = 0
for key, value in top_artists.items():
    idx += 1
    artist_info = sp.artist(value)
    if artist_info:
        print(
            f"""{idx}. {artist_info["name"]} 
    Image URL: {artist_info["images"][0]["url"]}
    Spotify Page: {artist_info["external_urls"]["spotify"]}"""
        )


# This is how I got the top 10 tracks for my account if you're curious!
# Unfortunately (maybe for the best) Spotify does not let me just give others access to my
# account data to users without an authorized spotify account,
# so I had to pivot to just grabbing it once like this
# and dumping it into a json file!

# scope = "user-top-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_top_artists()
# print("Danny's Top 10 Artists Right Now:")

# top_artists = {}
# for i, item in enumerate(results["items"]):
#     print(f"{i + 1}: {item['name']}: {item['id']}")
#     top_artists[item["name"]] = item["id"]
#     if i >= 9:
#         break

# with open("top_artists.json", "w") as f:
#     json.dump(top_artists, f, indent=4)
