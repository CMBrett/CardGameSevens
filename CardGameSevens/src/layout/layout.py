'''
Created on 9 Jun 2020

@author: Chris
'''
from deck.deck import Card, RANKS, SUITS
from prettytable import PrettyTable

class Layout(object):
    '''
    classdocs
    '''

    def __init__(self, suit, layout_num):
        '''
        Constructor
        '''
        self.suit = suit
        self.id = layout_num
        self.cards = []
        self.valid_cards = self.calculate_valid_cards()
    
    def __repr__(self):
        '''
        '''

        return [
            self.id,
            self.suit,
            self.get_lowest_card_rank(),
            self.get_seven_value(),
            self.get_highest_card_rank()
            ]
    
    def __str__(self):
        '''
        '''
        param_list = [
            self.id,
            self.suit,
            self.get_lowest_playable_card(),
            self.get_seven_value(),
            self.get_highest_playable_card()
        ]
        
        return ",".join(str(p) for p in param_list)
            
    
    def calculate_valid_cards(self):
        '''
        '''
        number_of_cards = len(self.cards)
        
        print("number of cards: ", number_of_cards)
        
        if len(self.cards) == 0:
            return [Card(7, self.suit)]
        else:
            valid_cards = [self.get_highest_playable_card(), self.get_lowest_playable_card()]
            print("calc valid_cards: ", valid_cards)
            return [c for c in valid_cards if c is not None]
    
    def get_lowest_card_rank(self):
        '''
        '''
        if len(self.cards) != 0: 
            return min(self.cards, key = lambda t: int(t.rank)).rank
        else:
            None

    def get_highest_card_rank(self):
        '''
        '''
        if len(self.cards) != 0: 
            return max(self.cards, key = lambda t: int(t.rank)).rank
        else:
            None

    def get_seven_value(self):
        '''
        '''
        if len(self.cards) != 0:
            return "layout active"
        else:
            return "Layout inactive"

    def get_lowest_playable_card(self):
        '''
        '''
        
        lowest_rank = self.get_lowest_card_rank()
        
        if lowest_rank:
            lowest_playable_rank = lowest_rank - 1
            
            if lowest_playable_rank in RANKS:
                return Card(lowest_playable_rank, self.suit)
        else:
            return None
    
    def get_lowest_playable_card_rank(self):
        '''
        '''
        low_card = self.get_lowest_playable_card()
        if low_card is not None:
            return low_card.rank
        else:
            return None
    
    def get_highest_playable_card(self):
        '''
        '''
        
        highest_rank = self.get_highest_card_rank()
        
        if highest_rank:
            highest_playable_rank = highest_rank + 1
            
            if highest_playable_rank in RANKS:
                return Card(highest_playable_rank, self.suit)
        else:
            return None

    def get_highest_playable_card_rank(self):
        '''
        '''
        high_card = self.get_highest_playable_card()
        if high_card is not None:
            return high_card.rank
        else:
            return None


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
                layout.id,
                layout.suit,
                layout.get_lowest_playable_card_rank(),
                layout.get_seven_value(),
                layout.get_highest_playable_card_rank()
                ])

        return table.get_string()

    def get_layout_by_suit(self, get_suit):
        '''
        '''
        for layout in self.layouts:
            if layout.suit == get_suit:
                return layout
        else:
            return None
    
    def get_layout_by_id(self, get_id):
        '''
        '''
        for layout in self.layouts:
            if layout.id == get_id:
                return layout
        else:
            return None
    

