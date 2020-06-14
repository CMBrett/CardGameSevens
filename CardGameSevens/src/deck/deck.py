'''
Created on 9 Jun 2020

@author: Chris
'''
import collections
import random

SUITS = ["C", "D", "H", "S"]
RANKS = [n for n in range(2, 15)]

class Card(object):
    '''
    '''
    
    def __init__(self, rank, suit):
        '''
        Constructor
        '''

        # Create named tuple instance 
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        '''
        '''
        return "({}, {})".format(str(self.rank), str(self.suit))
        
    @classmethod
    def create_from_user_cmd(cls, card_cmd_str):
        '''
        '''
        
        # Determine rank if rank is double digit
        if len(card_cmd_str) == 3:
            rank = card_cmd_str[0:1]
            suit = card_cmd_str[2]
        else:
            rank = card_cmd_str[0]
            suit = card_cmd_str[1]
        
        print("Creating card for command: {}, rank: {}, suit: {}".format(card_cmd_str, rank, suit))
        
        return cls(int(rank), suit)
    
    def in_list(self, lst):
        '''
        '''
        
        for lst_card in lst:
            rank_match = lst_card.rank == self.rank
            suit_match = lst_card.suit == self.suit
            if rank_match and suit_match:
                return True
        else:
            return False
    
    def remove_from_list(self, lst):
        '''
        '''
        for i, lst_card in enumerate(lst):
            rank_match = lst_card.rank == self.rank
            suit_match = lst_card.suit == self.suit
            if rank_match and suit_match:
                return lst.pop(i)
        else:
            return lst


class Deck(object):
    '''
    classdocs
    '''

    def __init__(self, deck_num=1):
        '''
        Constructor
        '''
        self.cards = [Card(r,s) for s in SUITS for r in RANKS] * deck_num

    def shuffle(self):
        '''
        Shuffles the cards.
        '''
        random.shuffle(self.cards)
    
    def deal(self, players):
        '''
        '''
        for i, player in enumerate(players):
            player.hand = self.cards[i::len(players)]
