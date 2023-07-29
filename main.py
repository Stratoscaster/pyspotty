from pyspotty import Pyspotty
from cli.spotify_cli import SpotifyCLI

def run():
    pysp = Pyspotty()
    cli = SpotifyCLI(pysp)
    cli.start()



if __name__ == '__main__':
    run()
