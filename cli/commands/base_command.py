from abc import ABC, abstractmethod
from json import dumps


class BaseCommand(ABC):

    def __init__(self, command_name: str, command_summary: str, help_text: list, user_input: str):
        if not isinstance(command_name, str) or not isinstance(command_summary, str) or not isinstance(help_text, list):
            self._command_configuration_warning()

        self.user_input = user_input
        self._parse_command_string(user_input)

    @abstractmethod
    def _parse_command_string(self, user_input):
        pass

    @abstractmethod
    def execute_command(self):
        pass

    def _get_self_dump(self):
        return dumps(self)

    def _command_configuration_warning(self):
        print(f'BaseCommand - command not properly configured: {self._get_self_dump()}')
