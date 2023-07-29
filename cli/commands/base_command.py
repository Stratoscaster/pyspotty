from __future__ import annotations  # Delay evaluation of typehints
from abc import ABC, abstractmethod
from json import dumps
from typing import Type


class BaseCommand(ABC):
    help_text = ['Command help_text not overridden.']
    command_summary = 'Command summary not overridden.'
    command_name = 'base_command'  # keyword for command
    subcommands = []
    INVALID_SUBCOMMAND = False, 'Invalid subcommand'

    def __init__(self, user_input: str):
        if not isinstance(self.class_type().command_name, str) \
                or not isinstance(self.class_type().command_summary, str) \
                or not isinstance(self.class_type().help_text, list):
            self._command_configuration_warning()

        self.user_input = user_input
        self._result = self._parse_command_string(user_input)

    def get_result(self):
        return self._result

    def _parse_command_string(self, user_input: str) -> tuple[bool, str]:
        # Here we have four branches that can occur
        # Case 1: This command has no more subcommands to parse down into
        # Case 2: This user_input cannot be parsed further (e.g. at the end of the user_input)
        # Case 3: The next token does not match an existing subcommand
        # Case 4: This command has a matching subcommand with the user_input, and
        #         we recursively create the subcommand class instance

        # In each of these cases we bubble up a result tuple[bool, str] to
        # determine success of the command at the top level

        if len(self.class_type().subcommands) == 0:
            return self.execute_command(user_input)  # Case 1

        next_parse = self.get_next_parse(user_input)
        token = next_parse[0]
        remainder = next_parse[1]
        if token == '':
            return self.execute_command(user_input)  # Case 2
        else:
            subcommand = self.get_subcommand(token)
            if subcommand is None:
                return self.execute_command(user_input)  # Case 3

            return subcommand(remainder).get_result()  # Case 4

    @abstractmethod
    def execute_command(self, *args) -> tuple[bool, str]:
        # Must return list of strings to display to output (or a template string inside of list)
        pass

    def _get_self_dump(self) -> str:
        return dumps(self)

    @classmethod
    def get_subcommands(cls) -> list['BaseCommand']:
        return cls.subcommands

    def _command_configuration_warning(self):
        print(f'BaseCommand - command not properly configured: {self._get_self_dump()}')

    def class_type(self):
        return type(self)

    @classmethod
    def has_subcommands(cls):
        return len(cls.get_subcommands()) > 0

    @classmethod
    def get_subcommand(cls, command_name) -> Type['BaseCommand']:
        for command in cls.get_subcommands():
            if command.command_name == command_name:
                return command

        return None

    @staticmethod
    def get_next_parse(user_input: str) -> tuple[str, str]:
        split = user_input.split(' ', 1)
        if len(split) < 2:
            return '', user_input
        return split[0], split[1]


