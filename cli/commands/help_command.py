from cli.commands.base_command import BaseCommand


# Use this as a template for future work
class HelpCommand(BaseCommand):
    help_text = [
        'help - See this text.',
        'status - Get your current play status'
    ]
    command_name = 'help'
    command_summary = 'A description of all main commands.'
    # TODO: Add list of subcommands that can be called, add subcommands to BaseCommand parent

    def __init__(self, pyspotty, user_input: str):
        super(HelpCommand, self).__init__(pyspotty, user_input)

    def execute_command(self, user_input):
        # my logic here and calling api package
        for line in HelpCommand.help_text:
            print(line)

