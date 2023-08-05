from base_command import BaseCommand


class StatusSubcommand(BaseCommand):
    command_name = 'status'
    command_summary = 'Get current status of playback.'
    help_text = [command_summary]

    def __init__(self, user_input):
        super(StatusSubcommand, self).__init__(user_input)

    def execute_command(self) -> tuple[bool, str]:
        return True, 'Playing next.'
