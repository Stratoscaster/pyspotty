from base_command import BaseCommand


# Use this as a template for future work
class HelpCommand(BaseCommand):
    help_text = [
        'This is a page to display when "help" is used on this command'
        'This is a second line to display'
    ]
    command_name = 'help'
    command_summary = 'A description of all main commands.'
    # TODO: Add list of subcommands that can be called, add subcommands to BaseCommand parent

    def __init__(self, user_input: str):
        super(HelpCommand, self).__init__(user_input)

    def execute_command(self):
        # my logic here and calling api package
        for line in HelpCommand.help_text:
            print(line)

