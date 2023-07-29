from pyspotty import Pyspotty
from tools.logging import log


class SpotifyCLI:

    def __init__(self, pyspotty: Pyspotty):
        self.pyspotty = pyspotty

        if not self.pyspotty.is_auth_success():
            log(f'Authentication token invalid: {self.pyspotty.auth_token}'
                f'\nPlease re-authenticate by deleting the auth_token.txt file.')
            quit()



