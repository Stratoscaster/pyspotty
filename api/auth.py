from requests import post, get, Response
from tools.security import Security
from tools.browser_interaction import open_url_in_browser
from urllib import parse
from tools.browser_callback import CallbackListener
from time import sleep
from threading import Thread

SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize?'
CALLBACK_PORT = 8069
REDIRECT_URL = f'http://localhost:{CALLBACK_PORT}/callback'
AUTH_TIMEOUT = 10 * 60

class RequestUserAuth:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id.replace('\n','').replace(' ','')
        self.client_secret = client_secret
        self.__security = Security()
        print(self.client_id)
        self.params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'scope': self.__security.compile_scope(),
            'redirect_uri': REDIRECT_URL,
            'state': self.__security.get_state(),
            'code_challenge_method': self.__security.get_challenge_method(),
            'code_challenge': self.__security.get_code_challenge()
        }
        # self.__credential_string = f'{self.client_id}:{self.client_secret}'

        self.response = None

    def call(self):
        # self.response = get(SPOTIFY_AUTH_URL, params=self.params)
        # open_url_in_browser(self.response.url)
        #
        # print('Spotify User-Auth-Request Received Request: ')
        # print(f'body: {self.response.request.body}')
        # print(f'headers: {self.response.request.headers}')
        # print(f'method: {self.response.request.method}')
        # print(f'url: {self.response.request.url}')
        # print('Spotify User-Auth-Request Response: ' + self.response.text)
        # print(open_url_in_browser(SPOTIFY_AUTH_URL + urlencode(self.params)))
        print('Client ID: [' + self.client_id + ']')
        callback_listener = CallbackListener()
        listener_thread = Thread(target=callback_listener.start)
        listener_thread.start()
        print('Please approve the OAuth Request in your web browser. :)')
        open_url_in_browser(f'https://accounts.spotify.com/authorize?client_id={self.client_id}&response_type=code&redirect_uri={REDIRECT_URL}')
        time_elapsed = 0
        while not callback_listener.callback_received:
            wait_time = 0.1
            time_elapsed += wait_time
            if wait_time >= AUTH_TIMEOUT:
                print('TIMED OUT WAITING FOR AUTH')
                callback_listener.stop_server()
            sleep(wait_time)

        callback_path = callback_listener.path
        path_dict = parse.urlsplit(callback_path.query)
        print('callback_path: ' + callback_path)
        print('callback_dict: ' + path_dict)


    def print_response(self):
        pass
        # for key, value in self.response.__dict__.items():
        #     print(f'{key}:{value}')
