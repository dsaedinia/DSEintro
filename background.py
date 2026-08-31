import spotipy
import json
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from spotipy.oauth2 import SpotifyClientCredentials

# from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

##################################
# Name: Daniel (Danny) Saedi Nia #
##################################
"""
Fun Fact:
I have lived many different places in my life. From Northeast Ohio, where I was born, to Southern Iran, where I spent 7 years. From there I moved back to the U.S., to Southern California, where I spent the next 11 years of my life. I am now living here in East Tennessee and have been for the past 2 years, and I will continue to be for at least as long as this PhD takes me.

I think that finding out someone's music taste is as good an introduction to a person as any, and so I thought I would share a small script to that retrieves and displays my top 10 Spotify artists right now.
"""

# This will be the artist image sizes. Both height and width are the same
SIZE = 500
# load global env variables --> spotipy API keys
load_dotenv()


def main():
    """Uses previously retrieved top spotify artists (commented out below) from my profile using Spotify Python API tool and displays each artist image and info through the terminal one by one.

    Note: you will need to close an image before the next can appear
    """

    # Get the dictionary of top artists and their IDs
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
            img_url = artist_info["images"][0]["url"]
            spotify_url = artist_info["external_urls"]["spotify"]
            artist_name = key

            print(
                f"""{idx}. {artist_info["name"]} 
        Image URL: {img_url}
        Spotify Page: {spotify_url}"""
            )

            # This is all to display the images one by one
            img = Image.open(urlopen(img_url))

            # compress the image
            img = img.resize((SIZE, SIZE), Image.LANCZOS)

            # Setting up tkinter window
            root = tk.Tk()
            root.title(f"{idx}. {artist_name}")
            root.resizable(width=True, height=True)

            tk_img = ImageTk.PhotoImage(img)
            tk.Label(
                root,
                image=tk_img,
                text=f"Spotify Link: {spotify_url}",
                pady="10",
                compound="top",
            ).pack()
            root.mainloop()


if __name__ == "__main__":
    main()

# This is how I got the top 10 tracks for my account if you're curious!
# Unfortunately (maybe for the best) Spotify does not let me give others access to my
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
