import requests
import json


class SpotifyBot:

    def __init__(self, token):
        self.token = token
        self.base = "https://api.spotify.com/"
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Bearer {}'.format(self.token)}

    def search_track(self, track):
        url = self.base + "v1/search?q={}&type=track".format(track)
        r = requests.get(url, headers=self.headers)
        return json.loads(r.content)

    def add_to_playlist(self, playlist_id, track_id):
        url = self.base + "v1/playlists/{}/tracks?uris=spotify%3Atrack%3A{}".format(playlist_id, track_id)
        r = requests.post(url, headers=self.headers)
        return json.loads(r.content)