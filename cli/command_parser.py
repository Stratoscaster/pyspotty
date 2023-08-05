from pyspotty import Pyspotty
from cli.commands.command_register import CommandRegister
from cli.commands.help_command import HelpCommand
class CommandParser:

    def __init__(self, pyspotty: Pyspotty):
        self.pyspotty = pyspotty
        self.command_reg = CommandRegister()
        self.register_custom_commands()

    def register_custom_commands(self):
        # If you want to mod this library and add your own commands, do it here as shown below.
        #   cli.commands.status_command.StatusCommand can be a good example of a simple GET request
        # E.g.
        # self.command_reg.add_command(my_root_keyword_for_command_no_spaces_string, MyBaseCommandImplementation)




        return

    def parse_input(self, user_input: str):
        root = user_input.split(' ')[0]
        trunk = user_input[len(root)-1: -1]
        OriginCommand = self.command_reg.get_command(root)
        if OriginCommand is None:
            print('Command is not a valid command. Please see the list of valid commands below: ')

        command = OriginCommand(self.pyspotty, trunk)


