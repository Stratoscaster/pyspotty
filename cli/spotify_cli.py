from pyspotty import Pyspotty
from tools.logging import log
from cli.command_parser import CommandParser

class SpotifyCLI:

    def __init__(self, pyspotty: Pyspotty):
        self.pyspotty = pyspotty
        self.is_running = True
        self.command_parser = CommandParser(self.pyspotty)
        if not self.pyspotty.is_auth_success():
            log(f'Authentication token invalid: {self.pyspotty.auth_token}'
                f'\nPlease re-authenticate by deleting the auth_token.txt file.')
            quit()

    def start(self):
        print('Welcome to SpotifyCLI! Use "help" for more information.')
        while self.is_running:
            print()
            user_input = input('$')
            self.command_parser.parse_input(user_input)


