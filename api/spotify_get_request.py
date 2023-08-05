import requests
import requests as req
from pyspotty import Pyspotty
from collections.abc import Callable
import json

class CurrentlyPlayingRequest:

    _API_PATH = 'me/player/currently-playing'

    def __init__(self, pyspotty: Pyspotty):
        self.pyspotty = pyspotty
        request = SpotifyGetRequest(self.pyspotty, self.handle_callback, self._API_PATH)

    def handle_callback(self, request):
        self.json = request.json()

        print(self.json)


class SpotifyGetRequest:
    _URL_BASE = 'https://api.spotify.com/v1/'


    def __init__(self, pyspotty: Pyspotty, callback:Callable, api_path: str, immediate_send: bool=True, params: dict=None):
        if api_path.startswith('/'):
            api_path = api_path[1:len(api_path)]
        self.api_path = api_path
        self.pyspotty = pyspotty
        self.params = params
        self.callback = callback
        if (immediate_send):
            self.send()

    def get_full_path(self):
        return self._URL_BASE + self.api_path

    def send(self):
        self.response = requests.get(self.get_full_path(), params=self.params, headers=self.pyspotty.get_auth_headers())
        request = self.response.request
        if self.pyspotty.debug_mode:
            print(f'''
    Request Object:
    Headers: {request.headers}
    Method: {request.method}
    Body: {request.body}
    Url: {request.url}
    ''')
        self.callback(self.response)
