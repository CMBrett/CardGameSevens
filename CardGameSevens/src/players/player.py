'''
Created on 9 Jun 2020

@author: Chris
'''

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
        
        player_string.append("Player: '{}'".format(self.player_id))
        player_string.append(newline)
        player_string.append("Rounds won: '{}'".format(self.rounds_won))
        player_string.append(newline)
        player_string.append("Current Cards: '{}'".format())
        player_string.append(newline)
        for card in self.hand:
            player_string.append(card)
            player_string.append(newline)

        return player_string
