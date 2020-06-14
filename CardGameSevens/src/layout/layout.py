'''
Created on 9 Jun 2020

@author: Chris
'''
from deck.deck import Card, RANKS, SUITS
from prettytable import PrettyTable
import itertools

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
    
    def __repr__(self):
        '''
        '''

        return [
            self.layout_num,
            self.suit,
            self._get_lowest_card_rank(),
            self._get_seven_value(),
            self._get_highest_card_rank()
            ]
    
    def calculate_valid_cards(self):
        '''
        '''
        if len(self.cards) == 0:
            return [Card(7, self.suit)]
        else:
            valid_cards = [self._get_highest_playable_card(), self._get_lowest_playable_card()]
            return [c for c in valid_cards if c is not None]
    
    def get_lowest_card_rank(self):
        '''
        '''
        if not len(self.cards) == 0: 
            min(self.cards, key = lambda t: int(t.rank)).rank
        else:
            None

    def get_highest_card_rank(self):
        '''
        '''
        if not len(self.cards) == 0: 
            max(self.cards, key = lambda t: int(t.rank)).rank
        else:
            None

    def get_seven_value(self):
        '''
        '''
        if len(self.cards) != 0:
            return "layout active"
        else:
            return "Layout inactive"

    def _get_lowest_playable_card(self):
        '''
        '''
        lowest_playable_rank = self._get_lowest_card_rank() - 1
        
        if lowest_playable_rank in RANKS:
            return Card(lowest_playable_rank, self.suit)
    
    def _get_highest_playable_card(self):
        '''
        '''
        highest_playable_rank = self._get_highest_card_rank() + 1
        
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

    def __str__(self):
        '''
        '''

        # Create table and add headers
        table = PrettyTable()        
        titles = ["Layout_ID", "Suit", "Lowest", "Seven", "Highest"]
        table.field_names = titles

        # Add str representation of each layout to the table
        for layout in self.layouts:
            table.add_row([
                layout.layout_num,
                layout.suit,
                layout.get_lowest_card_rank(),
                layout.get_seven_value(),
                layout.get_highest_card_rank()
                ])

        return table.get_string()

    def get_layout_by_suit(self, get_suit):
        '''
        '''
        for player in self.players:
            if player.player_id == get_suit:
                return player
        else:
            return None
    
    def get_layout_by_num(self, get_id):
        '''
        '''
        for layout in self.layouts:
            if layout.id == get_id:
                return layout
        else:
            return None
    

