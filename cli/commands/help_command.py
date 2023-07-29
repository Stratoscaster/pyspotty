from base_command import BaseCommand


# Use this as a template for future work
class HelpCommand(BaseCommand):

    def __init__(self, user_input: str):
        help_text = [
            'This is a page to display when "help" is used on this command'
            'This is a second line to display'
        ]
        # Add list of subcommands that can be called, add subcommands to BaseCommand parent
        command_name = 'help'
        command_summary = 'A description of all main commands.'
        super().__init__(command_name, command_summary, help_text, user_input)
