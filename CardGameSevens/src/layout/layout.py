'''
Created on 9 Jun 2020

@author: Chris
'''
from deck.deck import Card, RANKS, SUITS
from prettytable import PrettyTable

class Layout(object):
    '''Represents a single layout.'''

    def __init__(self, suit, layout_id):
        '''Creates Layout instance from suit and layout_id'''

        self.suit = suit
        self.id = layout_id
        self.cards = []
        self.valid_cards = self.calculate_valid_cards()
    
    def __repr__(self):
        '''Returns a printable representation of the object'''

        return [
            self.id,
            self.suit,
            self.get_lowest_card_rank(),
            self.get_seven_value(),
            self.get_highest_card_rank()
            ]
    
    def __str__(self):
        '''Returns a string representation of the object'''
        param_list = [
            self.id,
            self.suit,
            self.get_lowest_playable_card(),
            self.get_seven_value(),
            self.get_highest_playable_card()
        ]
        
        return ",".join(str(p) for p in param_list)
            
    
    def calculate_valid_cards(self):
        '''Calculates which cards can be played on layout.'''
        
        # If layout is not active then only card of rank 7 is valid
        if len(self.cards) == 0:
            return [Card(7, self.suit)]
        else:
            valid_cards = [self.get_highest_playable_card(), self.get_lowest_playable_card()]
            return [c for c in valid_cards if c is not None]
    
    def get_lowest_card_rank(self):
        '''Returns rank of lowest card in layout, if no cards then returns None'''

        if len(self.cards) != 0: 
            return min(self.cards, key = lambda t: int(t.rank)).rank
        else:
            None

    def get_highest_card_rank(self):
        '''Returns rank of highest card in layout, if no cards then returns None'''

        if len(self.cards) != 0: 
            return max(self.cards, key = lambda t: int(t.rank)).rank
        else:
            None

    def get_seven_value(self):
        '''Returns whether layout is active based on if a card has been played'''

        if len(self.cards) != 0:
            return "layout active"
        else:
            return "Layout inactive"

    def get_lowest_playable_card(self):
        '''Returns card instance for the lowest playable card'''

        lowest_rank = self.get_lowest_card_rank()
        
        if lowest_rank:
            lowest_playable_rank = lowest_rank - 1
            
            if lowest_playable_rank in RANKS:
                return Card(lowest_playable_rank, self.suit)
        else:
            return None
    
    def get_lowest_playable_card_rank(self):
        '''Returns card rank for the lowest playable card'''

        low_card = self.get_lowest_playable_card()
        if low_card is not None:
            return low_card.rank
        else:
            return None
    
    def get_highest_playable_card(self):
        '''Returns card instance for the highest playable card'''

        highest_rank = self.get_highest_card_rank()
        
        if highest_rank:
            highest_playable_rank = highest_rank + 1
            
            if highest_playable_rank in RANKS:
                return Card(highest_playable_rank, self.suit)
        else:
            return None

    def get_highest_playable_card_rank(self):
        '''Returns card rank for the highest playable card'''

        high_card = self.get_highest_playable_card()
        if high_card is not None:
            return high_card.rank
        else:
            return None


class Layouts(object):
    '''Represents a list of Layout objects, provides functions to perform on list.'''

    def __init__(self, deck_num):
        '''Creates all layouts to be used in-game based on deck_num'''

        suits = SUITS * deck_num
        self.layout_amount = len(suits)
        self.layouts = [Layout(suit, i) for i, suit in enumerate(suits)]

    def __str__(self):
        '''String representation to print table to cli.'''

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
    
    def get_layout_by_id(self, get_id):
        '''Returns layout based on layout_id'''
        for layout in self.layouts:
            if layout.id == get_id:
                return layout
        else:
            return None
