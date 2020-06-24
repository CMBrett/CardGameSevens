'''
Created on 11 Jun 2020

@author: Christopher Brett
'''

from deck.deck import Card

PASS_CMD = "pass"


class Command:
    '''Requests user input and validation of user commands'''

    def __init__(self, command_str, curr_layouts):
        '''Provides validation of user commands'''

        self.pass_cmd = False

        if command_str == PASS_CMD:
            self.pass_cmd = True
            self.card = None
            self.layout = None
        else:
            # Separate command string and pass to relevant constructor
            self.card = Card.create_from_user_cmd(command_str.split('L')[0])
            self.layout = curr_layouts.get_layout_by_id(
                int(command_str.split('L')[1])
                )

    def __str__(self):
        if self.pass_cmd:
            ret_str = PASS_CMD
        else:
            ret_str = "Card '{}' to Layout '{}'".format(self.card, self.layout)

        return ret_str

    @classmethod
    def get_user_command(cls, curr_layouts):
        '''Requests user input'''

        # Print command request
        print("Please enter next move: (format: <rank><suit>L<layout_id>)")
        print("(e.g 7CL0 to put the seven of clubs on layout_id 0)")

        # Collect user response
        user_input = input()

        try:
            return cls(user_input, curr_layouts)
        except Exception as exc:
            print(exc)

    @classmethod
    def get_computer_command(cls, com_input, curr_layouts):
        '''Converts computer move into Command instance'''

        return cls(com_input, curr_layouts)

    def is_valid(self, player_hand, verbose=False):
        '''Performs validation of user commands'''

        if self.pass_cmd:
            validity = True
        elif self.layout is None:
            validity = False
        else:

            # Calculate valid cards for layout
            layout_valid_cards = self.layout.calculate_valid_cards()

            # Perform checks whether card is in hand and specified layout
            card_in_layout_valid_cards = self.card in layout_valid_cards
            card_in_player_hand = self.card in player_hand
            card_in_hand_and_layout = (
                card_in_layout_valid_cards and card_in_player_hand
                )

            validity = card_in_hand_and_layout or self.pass_cmd

        if verbose:
            if validity:
                print("Command is valid")
            else:
                print("Command is invalid")

        return validity
