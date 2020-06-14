'''
Created on 11 Jun 2020

@author: Christopher Brett
'''

from deck.deck import Card

class Command(object):
    '''Requests user input and validation of user commands'''


    def __init__(self, command_str, curr_layouts):
        '''Provides validation of user commands'''

        print("Creating command from input: {}".format(command_str))

        # Separate command string and pass to relevant constructor
        self.card = Card.create_from_user_cmd(command_str.split('L')[0])
        self.layout = curr_layouts.get_layout_by_id(int(command_str.split('L')[1]))
        
        print("Command created: card: {}, layout: {}".format(self.card, self.layout))


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
            cls.get_user_command(curr_layouts)
            

    def is_valid(self, player_hand):
        '''Performs validation of user commands'''

        return self.card.in_list(self.layout.valid_cards) and self.card.in_list(player_hand)
    