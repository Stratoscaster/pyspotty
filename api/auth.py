from tools.security import Security
from tools.browser_interaction import open_url_in_browser
from urllib import parse
from tools.browser_callback import CallbackListener
from sys import exit

SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize?'
SPOTIFY_TOKEN_REQ_URL = 'https://accounts.spotify.com/api/token?'
CALLBACK_HOST = 'localhost'
CALLBACK_PORT = 8069
REDIRECT_URL = f'http://localhost:{CALLBACK_PORT}/callback'
AUTH_TIMEOUT = 10 * 60
CALLBACK_AUTH_PORT = 8070

# To host your own Spotify Web API creds, create an account at https://developer.spotify.com/, create an app, and add the following callbacks (exactly):
# http://localhost:8069/callback
# http://localhost:8070/callback
# You must also add your Spotify Web API credentials to the file pspotty/credentials.txt.
#       Enter exactly as follows but substitute your client_id:
#       id:<your client_id for your app goes here>
# This is not calling out to an external server, localhost is your loopback address (127.0.0.1) to your computer
# You probably already knew this haha


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


        self.response = None
        self.path_dict = None
        self.auth_token = None

    def call(self):
        print('Pyspotty Client ID: [' + self.client_id + ']')
        CallbackListener.start_server(self.verifier_callback, CALLBACK_HOST, CALLBACK_PORT)

        print('Please approve the OAuth Request in your web browser. :)')
        open_url_in_browser(f'{SPOTIFY_AUTH_URL}client_id={self.client_id}&response_type=code&redirect_uri={REDIRECT_URL}')




    def verifier_callback(self, server: CallbackListener, path: str):
        self._server = server
        if path is not None:
            self.verifier_code = self.process_path_for_token(path)

        else:
            print('CallbackListener: returned path was blank. Please try authenticating again.')
            quit()

        server.stop_server()
        self._call_auth_token_from_verifier()  # Once we have all necessary data we can make our callout.



    def _call_auth_token_from_verifier(self):
        CallbackListener.start_server(self.auth_callback, CALLBACK_HOST, CALLBACK_AUTH_PORT)
        print('Performing handshake...')
        open_url_in_browser(f'{SPOTIFY_TOKEN_REQ_URL}grant_type=authorizaton_code&code={self.verifier_code}&redirect_uri={REDIRECT_URL}&client_id={self.client_id}&code_verifier={self.__security.get_code_challenge()}')

    def auth_callback(self, server: CallbackListener, path: str):
        self._server = server
        if path is not None:
            self.auth_token = self.process_path_for_token(path)
        else:
            print('CallbackListener: returned path was blank. Please try authenticating again.')
            quit()

        server.stop_server()

    def process_path_for_token(self, path: str):
        split_query = parse.urlsplit(path).query.split('=')
        print(split_query[1])
        if len(split_query) > 1:
            print('AUTH Returned: ' + split_query[1])
            return split_query[1]
        else:
            print('RequestUserAuth error: Returned path was invalid: ' + path)
        return None




