'''
Created on 11 Jun 2020

@author: Chris
'''
from deck.deck import Card
from layout.layout import Layouts

class Command(object):
    '''
    classdocs
    '''


    def __init__(self, command_str, curr_layouts):
        '''
        Constructor
        '''

        print("Creating command from input: {}".format(command_str))

        # Separate command string and pass to relevant constructor
        self.card = Card.create_from_user_cmd(command_str.split('L')[0])
        self.layout = curr_layouts.get_layout_by_id(command_str.split('L')[1])


    @classmethod
    def get_user_command(cls, curr_layouts):
        '''
        '''

        # Print command request
        print("Please enter next move: (format: <rank><suit>L<layout_id>)")

        # Collect user response
        user_input = input()

        try:
            return cls(user_input, curr_layouts)
        except Exception:
            cls.get_user_command(curr_layouts)
            

    def is_valid(self):
        '''
        '''
        if self.card in self.layout.valid_cards:
            return True
        else:
            return False