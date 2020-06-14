'''
Created on 11 Jun 2020

@author: Christopher Brett
'''

from deck.deck import Card

PASS_CMD = "pass"

class Command(object):
    '''Requests user input and validation of user commands'''


    def __init__(self, command_str, curr_layouts):
        '''Provides validation of user commands'''

#         print("Creating command from input: {}".format(command_str))
        
        self.pass_cmd = False

        if command_str == PASS_CMD:
            self.pass_cmd = True
            self.card = None
            self.layout = None
        else:
            # Separate command string and pass to relevant constructor
            self.card = Card.create_from_user_cmd(command_str.split('L')[0])
            self.layout = curr_layouts.get_layout_by_id(int(command_str.split('L')[1]))
            
            print("Command created: card: {}, layout: {}".format(self.card, self.layout))

    def __str__(self):
        if self.pass_cmd:
            return PASS_CMD
        else:
            return "Card '{}' to Layout '{}'".format(self.card, self.layout)

    @classmethod
    def get_user_command(cls, curr_layouts):
        '''Requests user input'''

        # Print command request
        print("Please enter next move: (format: <rank><suit>L<layout_id>)")

        # Collect user response
        user_input = input()

        try:
            return cls(user_input, curr_layouts)
        except Exception as exc:
            print(exc)
#             cls.get_user_command(curr_layouts)
    
    @classmethod
    def get_computer_command(cls, com_input, curr_layouts):
        '''Converts computer move into Command instance'''

        return cls(com_input, curr_layouts)

    def is_valid(self, player_hand):
        '''Performs validation of user commands'''

        if self.pass_cmd:
            validity = True
        else:
            card_in_layout_valid_cards = self.card.in_list(self.layout.calculate_valid_cards())
            card_in_player_hand = self.card.in_list(player_hand)
            validity = (card_in_layout_valid_cards and card_in_player_hand) or self.pass_cmd

        if validity:
            print("Command is valid")
        else:
            print("Command is invalid")

        return validity
    