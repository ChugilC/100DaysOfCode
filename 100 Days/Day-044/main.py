from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
APP_CLIENT_ID = os.getenv("CLIENT_ID")
APP_CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Scrape Songs names
print("Welcome to billboard's Top 100")
song_date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{song_date}/")
data = response.text

soup = BeautifulSoup(data, 'html.parser')
headings = soup.find_all(name="h3", class_="a-no-trucate")

song_names = [heading.string.strip() for heading in headings]

# Auth - Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id = APP_CLIENT_ID,
    client_secret= APP_CLIENT_SECRET,
    show_dialog = True,
    redirect_uri = "http://example.com",
    cache_path = "100 Days/Day-044/token.txt"
))

user_id = sp.current_user()["id"]

# Search songs in spotify
song_uris = []
year = song_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"Billboard's 100 on {song_date}", public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)