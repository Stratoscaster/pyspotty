from requests import post, Response
import json
spotify_auth_url = 'https://accounts.spotify.com/api/token'

class GetAuthToken:
    def __init__(self, client_id:str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.json = {
            'url': 'https://accounts.spotify.com/api/token',
            'headers': {
                'Authorization': f'Basic {self.client_id}:{self.client_secret}',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'form': {
                'grant_type': 'client_credentials'
            },
            'json': True
        }
        self.response = None

    def call(self):
        self.response = post(spotify_auth_url, json=self.json)
        print('Spotify Auth-Request Response: ' + self.response.text)

    def print_response(self):
        for key, value in self.response.__dict__.items():
            print(f'{key}:{value}')
