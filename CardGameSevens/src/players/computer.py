'''
Created on 11 Jun 2020

@author: Chris
'''
from players.player import Player

class Computer(Player):
    '''
    classdocs
    '''
    
    def __init__(self, player_id, level):
        '''
        '''
        self.player_id = player_id
        self.level = level
    
    def calculate_move(self):
        '''
        '''
        pass
        