'''
Created on 11 Jun 2020

@author: Chris
'''
from players.player import Player

class Computer(Player):
    '''Computer Player type uses a different method to provide moves'''

    def __init__(self, player_id, level):
        '''Creates a computer player with a designated difficulty level.'''

        self.player_id = player_id
        self.level = level
        self.hand = []

    def request_command(self, curr_layouts):
        '''Performs command calculation when computer player's turn'''
        # TODO: move logic for computer
        pass

    def calculate_move(self):
        '''Used to calculate move based on difficulty level'''
        # TODO: move logic for computer
        pass
        