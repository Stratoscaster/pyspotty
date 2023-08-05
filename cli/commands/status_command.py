from cli.commands.base_command import BaseCommand
from api.spotify_get_request import CurrentlyPlayingRequest


# This can be used as an example of how to add new commands to pyspotty

class StatusSubcommand(BaseCommand):
    command_name = 'status'
    command_summary = 'Get current status of playback.'
    help_text = [command_summary]

    # Create the init exactly as this unless other data processing is needed for your call
    # This will attach your pyspotty instance to the commands and allow them access to make calls
    def __init__(self, pyspotty, user_input):
        super(StatusSubcommand, self).__init__(pyspotty, user_input)


    # Import your get or post request and pass through relevant data
    # execute_command should always accept user_input as string (see BaseCommand_parse_command_string() as to why)
    def execute_command(self, user_input) -> tuple[bool, str]:
        self.request = CurrentlyPlayingRequest(self.pyspotty)
        self.response = self.request.json
