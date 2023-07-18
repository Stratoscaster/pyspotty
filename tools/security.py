import string
import random
from hashlib import sha256
import base64


class Security:

    PKCE_LENGTH = 128
    CHALLENGE_METHOD = 'S256'
    SCOPES = [
        'user-read-playback-state',
        'user-modify-playback-state',
        'user-read-currently-playing',
        'app-remote-control',
        'streaming',
        'playlist-read-private',
        'playlist-read-collaborative',
        'playlist-modify-private',
        'playlist-modify-public',
        'user-read-playback-position',
        'user-top-read',
        'user-read-recently-played',
        'user-library-modify',
        'user-library-read',
        'user-read-email',
        'user-read-private'
    ]
    def __init__(self):
        self.__code_challenge_verifier = self.__generate_hashed_code_challenge_verifier()
        self.__state = Security.__generate_random_state()
        self.__challenge_method = Security.CHALLENGE_METHOD
        self.__PKCE_LENGTH = Security.PKCE_LENGTH

    def get_code_challenge(self):
        return self.__code_challenge_verifier

    @staticmethod
    def compile_scope():
        scope_string = ''
        for scope in Security.SCOPES:
            scope_string += scope + ' '
        scope_string = scope_string[0:-1]
        return scope_string

    def get_state(self):
        return self.__state

    def get_challenge_method(self):
        return self.__challenge_method

    def get_pkce_length(self):
        return self.__PKCE_LENGTH

    @staticmethod
    def generate_random_string(length: int):
        content = ''
        possible_chars = string.ascii_letters + string.digits
        for i in range(length):
            content += random.choice(possible_chars)

        return content

    @staticmethod
    def base64_encode_string(data):
        string_base64 = None
        if isinstance(data, str):
            string_bytes = data.encode()    # Encode into bytes (default behavior)
            string_base64 = base64.urlsafe_b64encode(string_bytes)
        elif isinstance(data, bytes):
            string_base64 = base64.urlsafe_b64encode(data)
        else:
            print('[Fatal]Error during base64 encoding: given data was not of type bytes or string.')
        return string_base64.decode()   # Decode bytes back into string

    def __generate_hashed_code_challenge_verifier(self):
        random_string = Security.generate_random_string(Security.PKCE_LENGTH)   # Get our randomized string
        self.__code_verifier_original = random_string
        b64_string = Security.base64_encode_string(random_string).encode()   # convert to b64 encoded string & encode to bytes
        sha256_bytes = sha256(b64_string).digest()  # encrypt with SHA-256 and digest into b64 bytes
        # sha256_string = sha256_bytes.decode()   # decode bytes into string

        return Security.base64_encode_string(sha256_bytes)

    @staticmethod
    def __generate_random_state():
        return Security.generate_random_string(16)

