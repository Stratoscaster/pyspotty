import cli.commands as commands


class CommandCompiler:

    def __init__(self, user_input: str):
        for pyfile in commands:
            print(pyfile)