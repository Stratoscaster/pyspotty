from pyspotty import Pyspotty
from cli.spotify_cli import SpotifyCLI

def run():
    pysp = Pyspotty(debug_mode=True)    # Enable with debug mode if desired
    cli = SpotifyCLI(pysp)
    cli.start()



if __name__ == '__main__':
    run()
