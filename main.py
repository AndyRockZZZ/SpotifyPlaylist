import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 1.  Scraping the Billboard Top 100
date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/"
print("Searching Top 100 songs.")
requests_response = requests.get(url=f"{url}{date_input}")
soup = BeautifulSoup(requests_response.text, "html.parser")

chart_row = soup.findAll(name="li", class_="lrv-u-width-100p")
song_titles = [chart.find(name="h3", id='title-of-a-story').getText().strip() for chart in chart_row if
              chart.find(name="h3", id='title-of-a-story') is not None]
song_artists = [chart.find(name="span").getText().strip() for chart in chart_row
               if not chart.find(name="span").getText().strip().isnumeric()
               and chart.find(name="span").getText().strip() != '-']

# 2. Authentication and Spotify
print("\nAuthenticating Spotify.")
CLIENT_ID = os.environ.get('CLIENTID')
CLIENT_SECRET = os.environ.get('CLIENT_SEC')

scope = 'playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope=scope))
# 3. Verify the songs exist on Spotify
USER_ID = sp.current_user()["id"]
song_uris = []
print("\nVerifying Songs on Spotify.")

for song in song_titles:
    query = f"track:{song} year:{date_input.split('-')[0]}"
    search_type = "track"

    search_track = sp.search(q=query, type="track")
    try:
        uri = search_track["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Song - ({song}) - doesn't exist in Spotify. Skipped.")

print("The songs are verified.\n")

# 4. Create new playlist
new_playlist = sp.user_playlist_create(user=USER_ID, name=f"Billboard Top 100 ({date_input})", public=False)
playlist_id = new_playlist["id"]
result = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris, position=None)
print(result)
print(f"New playlist added called Billboard Top 100 ({date_input}).")
