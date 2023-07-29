from tools.security import Security
from tools.browser_interaction import open_url_in_browser
from urllib import parse
from tools.browser_callback import CallbackListener
from time import sleep
from threading import Thread

SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize?'
CALLBACK_PORT = 8069
CALLBACK_ADDRESS = 'localhost'
REDIRECT_URL = f'http://localhost:{CALLBACK_PORT}/callback'
AUTH_TIMEOUT = 10 * 60


class RequestUserAuth:
    def __init__(self, client_id: str, callback_address: tuple[str, int] = None):
        self.client_id = client_id.replace('\n', '').replace(' ', '')
        self._callback_address = callback_address
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

        self.response = None

    def call(self):
        print('Client ID: [' + self.client_id + ']')
        callback_listener = CallbackListener(callback_address=self._callback_address)
        listener_thread = Thread(target=callback_listener.start)
        listener_thread.start()
        print('Please approve the OAuth Request in your web browser. :)')
        open_url_in_browser(
            f'https://accounts.spotify.com/authorize?client_id={self.client_id}&response_type=code&redirect_uri={REDIRECT_URL}')
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


