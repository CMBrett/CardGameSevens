'''
Created on 11 Jun 2020

@author: Chris
'''

from players.human import Human
from players.computer import Computer


class Players(object):
    '''
    classdocs
    '''

    def __init__(self, player_num, human_num, comp_levels):
        '''
        '''
        # Create Human and Computer players accordingly
        self.players = [
            Human(i) if i < human_num else Computer(i, comp_levels[i])
            for i in range(player_num)
            ]
    
    def clear_hands(self):
        '''
        '''
        # Call the "clear_hands" method on each player instance
        map(lambda x: x.clear_hand(), self.players)
    
    def get_player_by_id(self, get_id):
        '''
        '''
        for player in self.players:
            if player.player_id == get_id:
                return player
        else:
            return None
