from pyspotty import Pyspotty
from tools.logging import log


class SpotifyCLI:

    def __init__(self, pyspotty: Pyspotty):
        self.pyspotty = pyspotty
        self.is_running = True
        if not self.pyspotty.is_auth_success():
            log(f'Authentication token invalid: {self.pyspotty.auth_token}'
                f'\nPlease re-authenticate by deleting the auth_token.txt file.')
            quit()

    def start(self):
        print('Welcome to SpotifyCLI! Use "help" for more information.')
        while self.is_running:
            print()
            user_input = input('$')
            self.build_command # Add logic for building commands using base command
