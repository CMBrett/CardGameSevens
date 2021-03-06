'''
Created on 9 Jun 2020

@author: Christopher Brett
'''
from players.player import Player
from command.command import Command


class Human(Player):
    '''Provides user_input request for human player'''

    def request_command(self, curr_layouts):
        '''Prompts user for input when player's turn and validates the input'''

        self.current_command = Command.get_user_command(curr_layouts)

        # Check that command is valid
        if not self.current_command.is_valid(self.hand):
            self.request_command(curr_layouts)

        return self.current_command
