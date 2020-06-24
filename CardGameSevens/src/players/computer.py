'''
Created on 11 Jun 2020

@author: Christopher Brett
'''
import random
from players.player import Player
from command.command import Command, PASS_CMD


class Computer(Player):
    '''Computer Player type uses a different method to provide moves'''

    def __init__(self, player_id, level):
        '''Creates a computer player with a designated difficulty level.'''

        super(Computer, self).__init__(player_id)
        self.level = level
        self.valid_cards = []

    def request_command(self, curr_layouts):
        '''Performs command calculation when computer player's turn.'''

        # Assign current layouts and current command
        self.current_layouts = curr_layouts
        self.get_computer_command()

        # Check that command is valid
        if not self.current_command.is_valid(self.hand):
            self.request_command(curr_layouts)

        return self.current_command

    def get_computer_command(self):
        '''Calculates computer command.'''
        self.current_command = Command.get_computer_command(
            self.calculate_move(), self.current_layouts)

    def calculate_move(self):
        '''Used to calculate move determined by difficulty level.'''

        # Get valid_cards for layout
        layout_valid_cards = [
            (i, layout.calculate_valid_cards())
            for i, layout in enumerate(self.current_layouts)
            ]

        # Check for possible moves
        for layout_id, valid_cards in layout_valid_cards:
            possible_moves = [
                (layout_id, c) for c in valid_cards if c in self.hand
                ]

        # Make choice based on difficulty
        if self.level > 1:
            chosen_move = self.get_level_two_move(possible_moves)
        else:
            chosen_move = self.get_level_one_move(possible_moves)

        # Print computer move to cli
        print("Computer move: ", chosen_move)

        return chosen_move

    def get_level_one_move(self, moves):
        '''Provides computer move of level one difficulty'''

        # Choose a random move
        if len(moves) > 0:
            chosen_move = random.choice(moves)
        else:
            return PASS_CMD

        # Convert to command_str and return
        return self.chosen_move_to_cmd_str(chosen_move)

    def get_level_two_move(self, moves):
        '''Provides computer move of level two difficulty'''

        # Remove all 7,8,9 cards if other cards are valid
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

        return self.chosen_move_to_cmd_str(chosen_move)

    @staticmethod
    def chosen_move_to_cmd_str(chosen_move):
        '''write a command string for the computer move'''

        return "".join([
            str(chosen_move[1].rank),
            chosen_move[1].suit,
            "L" + str(chosen_move[0])
            ])
