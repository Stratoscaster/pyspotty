import requests
import requests as req


class SpotifyGetRequest:
    URL_BASE = 'https://api.spotify.com/v1/'
    API_PATHS = {
        'currently_playing': 'me/player/currently-playing'
    }
    PATH_CURRENTLYPLAYING = 'currently_playing'

    def __init__(self, api_path_name: str):
        if api_path_name not in SpotifyGetRequest.API_PATHS:
            print(f'{api_path_name} is an invalid get method.')
            return

        self.api_path = SpotifyGetRequest.API_PATHS.get(api_path_name)

    def send(self):
        requests.get()
