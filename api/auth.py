from tools.security import Security
from tools.browser_interaction import open_url_in_browser
from urllib import parse
from tools.browser_callback import CallbackListener


SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize?'
CALLBACK_HOST = 'localhost'
CALLBACK_PORT = 8069
REDIRECT_URL = f'http://localhost:{CALLBACK_PORT}/callback'
AUTH_TIMEOUT = 10 * 60


class RequestUserAuth:
    def __init__(self, client_id: str, callback_address: tuple[str, int] = None):
        self.client_id = client_id.replace('\n', '').replace(' ', '')
        self._callback_address = callback_address
        self.__security = Security()
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
        self.path_dict = None
        self.auth_token = None

    def call(self):
        print('Pyspotty Client ID: [' + self.client_id + ']')
        CallbackListener.start_server(self.listener_callback, CALLBACK_HOST, CALLBACK_PORT)

        print('Please approve the OAuth Request in your web browser. :)')
        open_url_in_browser(f'https://accounts.spotify.com/authorize?client_id={self.client_id}&response_type=code&redirect_uri={REDIRECT_URL}')

    def listener_callback(self, server: CallbackListener, path: str):
        if path is not None:
            self.process_path_for_auth_code(path)
            server.stop_server()
        else:
            print('CallbackListener: returned path was blank. Please try authenticating again.')

    def process_path_for_auth_code(self, path: str):
        split_query = parse.urlsplit(path).query.split('=')
        if len(split_query) > 1:
            self.auth_token = split_query[1]
        else:
            print('RequestUserAuth error: Returned path was invalid: ' + path)



