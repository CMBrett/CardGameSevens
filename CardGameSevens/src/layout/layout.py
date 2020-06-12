'''
Created on 9 Jun 2020

@author: Chris
'''
from deck.deck import Card, RANKS, SUITS

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

class Layouts(object):
    '''
    classdocs
    '''


    def __init__(self, deck_num):
        '''
        Constructor
        '''
        self.layout_amount = deck_num * 4
        suits = SUITS * deck_num
        self.layouts = [Layout(suit, i) for i, suit in enumerate(suits)]
    
    def get_layout_by_suit(self):
        '''
        '''
        pass
    
    def get_layout_by_num(self):
        '''
        '''
        pass

