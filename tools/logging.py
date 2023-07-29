from tools import time_tools


def log(msg: str):
    print(f'{time_tools.get_time_as_str()} - [SpotifyCLI]: {msg}')
