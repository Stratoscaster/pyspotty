from base_command import BaseCommand


class NextSubcommand(BaseCommand):
    command_name = 'next'
    command_summary = 'Play next song.'
    help_text = [command_summary]

    def __init__(self, user_input):
        super(NextSubcommand, self).__init__(user_input)

    def execute_command(self) -> tuple[bool, str]:
        return True, 'Playing next.'


class PreviousSubcommand(BaseCommand):
    command_name = 'previous'
    command_summary = 'Play previous song.'
    help_text = [command_summary]

    def __init__(self, user_input):
        super(PreviousSubcommand, self).__init__(user_input)

    def execute_command(self, *args) -> tuple[bool, str]:
        return True, 'Playing previous.'


class PlayCommand(BaseCommand):
    command_name = 'play'
    command_summary = 'Play or seek songs. Use search to find a specific song to add to queue or playlist'
    help_text = [f'''{command_summary}
    play - Toggle between pausing and playing the current song.
    play next - Play the next song in queue.
    play previous - Play the previous song in queue.
    ''']
    subcommands = [NextSubcommand]

    def __init__(self, user_input):
        super(PlayCommand, self).__init__(user_input)

    def execute_command(self, *args) -> tuple[bool, str]:
        return True, 'Toggling play'
