'''
Created on 9 Jun 2020

@author: Chris
'''
from players.human import Human
from players.computer import Computer
from utility.utility import contains

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, player_id):
        '''
        Constructor
        '''
        self.player_id = player_id
        self.hand = []
        self.rounds_won = 0
    
    def clear_hand(self):
        self.hand = []

    def __str__(self):
        '''
        '''
        player_string = ""
        newline = "\n"
        
        player_string.append("Player: '" + self.player_id + "'")
        player_string.append(newline)
        player_string.append("Rounds won: '{}'".format(self.rounds_won))
        player_string.append(newline)
        player_string.append("Current Cards: '{}'".format())
        player_string.append(newline)
        for card in self.hand:
            player_string.append(card)
            player_string.append(newline)

        return player_string


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
