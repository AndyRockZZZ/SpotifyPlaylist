# Spotify Playlist
Create a new Spotify Playlist of Top 100 Songs from billboard.com<br>

<p>I used a website url "https://www.billboard.com/charts/hot-100/" to get my Top 100 songs.<br>For the request, You will need to add the date like this "2023-11-10" (Year-Month-Day) into the URL.<br> https://www.billboard.com/charts/hot-100/2023-11-10/</p>
<p>I used a Web Scraping tool called <strong>Beautfiful Soup</strong> to pull data out of HTML and XML files. So for the request, I will parse the JSON data into HTML.</p>
<p>For the Authentication, if you have Spotify account, then go to this website called <a href="https://developer.spotify.com/dashboard">Spotify for Developers</a>, to create an App and get your <strong>Client ID</strong> & <strong>Secret Code</strong>.</p>

# Example
<p>The date that I want to use for my playlist is "2016-11-12".<br>Send request to the Billboard URL. This is the page to web scrap the Top 100 Songs.<br><br>![URL Image](https://github.com/AndyRockZZZ/SpotifyPlaylist/assets/25687861/e3d2386f-e0aa-49f7-aa8a-78c27f48fe39)![Top 100 Songs](https://github.com/AndyRockZZZ/SpotifyPlaylist/assets/25687861/edc48dd0-7119-434a-aca9-6387c0c30ea9)<br><br>The result of the requested songs into a playlist.<br><br>![Spotify Playlist](https://github.com/AndyRockZZZ/SpotifyPlaylist/assets/25687861/ee569833-50ee-432b-9488-9d006fefdda0)</p>

# Have a go
<p>If you like to have go with this project, you're welcome to download my code into your Python or Pycharm software.<br>The things you need are:
  <ul>
    <li>Spotify Account for making the playlist.</li>
    <li>Go to Spotify Developer Dashboard to create an App, and get your <strong>Client ID</strong> & <strong>Secret Code</strong>. Copy and replace my Client ID and Secret.</li>
    <li>Python Packages to Install:</li>
    <ul>
      <li>Requests</li>
      <li>Beautiful Soup</li>
      <li>Spotipy - <a href="https://pypi.org/project/spotipy/">Documentation</a></li>
    </ul>
  </ul>
</p>

