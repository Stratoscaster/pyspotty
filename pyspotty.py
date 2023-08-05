from api.auth import RequestUserAuth
from os import path
from time import sleep


auth_token_filename = 'authtoken.txt'
credentials_filename = 'credentials.txt'


class Pyspotty:

    def __init__(self, force_reauth=False, debug_mode=False):
        print('Starting Pyspotty...')
        credentials = Pyspotty.get_credentials()
        if credentials is None or credentials['id'] is None:
            print('Credentials.txt file must have one line for '
                  'client_id:\nid:<your client_id here>')
            quit()
        self.debug_mode = debug_mode
        self.client_id = credentials['id']

        # Attempt to load pre-existing auth token
        self.auth_token = Pyspotty.load_auth_token()

        # If re-auth forced or auth token doesn't exist, request user auth
        if force_reauth or self.auth_token is None:
            token_request = RequestUserAuth(self.client_id)
            token_request.call()
            while token_request.auth_token is None:
                sleep(0.5)
            self.auth_token = token_request.auth_token
            self.save_auth_token(self.auth_token)

    def get_auth_token(self):
        return self.auth_token

    def get_auth_headers(self):
        print(self.get_auth_token())
        return {'Authorization': f'Bearer {self.get_auth_token()}'}

    def is_auth_success(self):
        return self.auth_token is not None

    @staticmethod
    def get_credentials():
        if not Pyspotty.credentials_file_exists():
            return None
        mappings = {}
        with open('credentials.txt', 'r') as f:
            content = f.readlines()

            for line in content:
                try:
                    key, value = line.split(':')
                    mappings[key] = value
                except BaseException as e:
                    print(f'Configuration error:{e}')
                    continue
        return mappings

    @staticmethod
    def save_auth_token(auth_token):
        if auth_token is None or auth_token == '':
            return
        with open(auth_token_filename, 'w') as f:
            f.write(auth_token)

    @staticmethod
    def load_auth_token():
        if not Pyspotty.auth_token_file_exists():
            return None
        with open(auth_token_filename, 'r') as f:
            token = f.readline()

        return token

    @staticmethod
    def auth_token_file_exists():
        return path.exists(auth_token_filename) and path.isfile(auth_token_filename)

    @staticmethod
    def credentials_file_exists():
        return path.exists(credentials_filename) and path.isfile(credentials_filename)
