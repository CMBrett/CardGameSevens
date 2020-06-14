'''
Created on 9 Jun 2020

@author: Chris
'''
from prettytable import PrettyTable
from deck.deck import SUITS, CARD_VALS
from utility import utility

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
        '''
        '''
        
        self.hand = []

    def sort_hand(self):
        '''
        '''
        self.hand = sorted(self.hand, key= lambda h:h.rank)

    def check_if_winner(self):
        '''
        '''
        
        if len(self.hand) == 0:
            return True
        else:
            return False

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

    def get_hand_table(self):
        '''
        '''

        # Create table and add headers
        table = PrettyTable()

        # Add str representation of each layout to the table
        clubs_col = self.card_val(sorted([c.rank for c in self.hand if c.suit == "C"]))
        diamo_col = self.card_val(sorted([c.rank for c in self.hand if c.suit == "D"]))
        heart_col = self.card_val(sorted([c.rank for c in self.hand if c.suit == "H"]))
        spade_col = self.card_val(sorted([c.rank for c in self.hand if c.suit == "S"]))

        columns = [clubs_col, diamo_col, heart_col, spade_col]
        
        longest_list_length = len(max(columns, key=len))
        
        for i, col in enumerate(columns):
            
            if len(col) < longest_list_length:
                columns[i] = utility.pad(col, "", longest_list_length)
            table.add_column(SUITS[i], columns[i], align='c', valign='m')

        return table.get_string()
    
    def card_val(self, ranks):
        '''
        '''
        
        for i, r in enumerate(ranks):
            if r > 10:
                ranks[i] = CARD_VALS[r]
                 
        return ranks
        

