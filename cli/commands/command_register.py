from cli.commands.status_command import StatusSubcommand
from cli.commands.base_command import BaseCommand
from cli.commands.help_command import HelpCommand

# Recommended: Do not modify, add commands in the cli.command_engine.CommandEngine class
# Here are where the included commands for this CLI are included. Keeping your commands separate can avoid confusion.
class CommandRegister:

    def __init__(self):
        self.commands = {}
        self.add_default_commands()

    def add_command(self, command_name, command_class: BaseCommand):
        self.commands[command_name] = command_class

    def add_default_commands(self):
        self.commands[HelpCommand.command_name] = HelpCommand
        self.commands[StatusSubcommand.command_name] = StatusSubcommand

    def get_command(self, command_name):
        if command_name in self.commands:
            return self.commands[command_name]
        else:
            return None

