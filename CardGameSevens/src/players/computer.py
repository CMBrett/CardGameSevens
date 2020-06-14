'''
Created on 11 Jun 2020

@author: Christopher Brett
'''
from players.player import Player
from command.command import Command, PASS_CMD
import random

class Computer(Player):
    '''Computer Player type uses a different method to provide moves'''

    def __init__(self, player_id, level):
        '''Creates a computer player with a designated difficulty level.'''

        self.player_id = player_id
        self.level = level
        self.hand = []
        self.valid_cards = []

    def request_command(self, curr_layouts):
        '''Performs command calculation when computer player's turn.'''

        # Assign current layouts and current command
        self.current_layouts = curr_layouts
        self.get_computer_command()

        # Check that command is valid
        if self.current_command.is_valid(self.hand):
            return self.current_command
        else:
            self.request_command(curr_layouts)

    def get_computer_command(self):
        ''''''
        self.current_command = Command.get_computer_command(
            self.calculate_move(), self.current_layouts)

    def calculate_move(self):
        '''Used to calculate move determined by difficulty level.'''

        # Get valid_cards for layout
        layout_valid_cards =[
            (i, layout.calculate_valid_cards()) for i, layout in enumerate(self.current_layouts)
            ]

        # Check for possible moves
        for layout_id, valid_cards in layout_valid_cards:
            possible_moves = [(layout_id, c) for c in valid_cards if c.in_list(self.hand)]

        # Make choice based on difficulty
        if self.level > 1:
            return self.get_level_two_move(possible_moves)
        else:
            return self.get_level_one_move(possible_moves)

    def get_level_one_move(self, moves):
        '''Provides computer move of level one difficulty'''

        # Choose a random move
        if len(moves) > 0:
            chosen_move = random.choice(moves)
        else:
            return PASS_CMD

        # Convert to command_str
        cmd_str = self.chosen_move_to_cmd_str(chosen_move)

        print("computer move: ", cmd_str)

        return cmd_str

    def get_level_two_move(self, moves):
        '''Provides computer move of level two difficulty'''
        
        # Remove all 7,8,9 cards if there are other cards possible in that layout
        for i, move in enumerate(moves):
            cards = move[1]
            seven_eight_nine_cards = [c for c in cards if c.rank in [6, 7, 8]]
            remaining_card_len = (len(cards)-len(seven_eight_nine_cards))

            if len(seven_eight_nine_cards) != 0 and remaining_card_len != 0:
                for card in seven_eight_nine_cards:
                    cards = card.remove_from_list(cards)

                moves[i] = cards
        
        if len(moves) > 0:
            chosen_move = random.choice(moves)
        else:
            return PASS_CMD

        cmd_str = self.chosen_move_to_cmd_str(chosen_move)

        print("computer move: ", cmd_str)

        return cmd_str

    def chosen_move_to_cmd_str(self, chosen_move):
        '''write a command string for the computer move'''
        
        return str(chosen_move[1].rank) + chosen_move[1].suit + "L" + str(chosen_move[0])
