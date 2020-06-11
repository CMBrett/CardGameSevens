'''
Created on 9 Jun 2020

@author: Chris
'''
from deck.deck import Card, RANKS

class Layout(object):
    '''
    classdocs
    '''


    def __init__(self, suit, layout_num):
        '''
        Constructor
        '''
        self.suit = suit
        self.layout_num = layout_num
        self.cards = []
        self.valid_cards = self.calculate_valid_cards()
    
    def calculate_valid_cards(self):
        '''
        '''
        if len(self.cards) == 0:
            return [Card(7, self.suit)]
        else:
            valid_cards = [self._get_highest_playable_card(), self._get_lowest_playable_card()]
            return [c for c in valid_cards if c is not None]
    
    def _get_lowest_playable_card(self):
        '''
        '''
        lowest_playable_rank = min(self.cards, key = lambda t: int(t.rank)).rank - 1
        
        if lowest_playable_rank in RANKS:
            return Card(lowest_playable_rank, self.suit)
    
    def _get_highest_playable_card(self):
        '''
        '''
        highest_playable_rank = max(self.cards, key = lambda t: int(t.rank)).rank + 1
        
        if highest_playable_rank in RANKS:
            return Card(highest_playable_rank, self.suit)
