'''
Created on 9 Jun 2020

@author: Christopher Brett
'''

import random

SUITS = ["C", "D", "H", "S"]
RANKS = [n for n in range(2, 15)]
CARD_VALS = {11: "J", 12: "Q", 13: "K", 14: "A"}

class Card(object):
    '''Represents a playing card'''
    
    def __init__(self, rank, suit):
        '''Creates Card instance from given rank and suit'''

        # Create named tuple instance 
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        '''Returns a printable representation of the object'''

        return "({}, {})".format(str(self.rank), str(self.suit))
        
    @classmethod
    def create_from_user_cmd(cls, card_cmd_str):
        '''Creates a card instance based on user input string'''
        
        # Determine rank if rank is double digit
        if len(card_cmd_str) == 3:
            rank = card_cmd_str[0:1]
            suit = card_cmd_str[2]
        else:
            rank = cls._get_rank_from_user_cmd(card_cmd_str[0])
            suit = card_cmd_str[1]
        
        print("Creating card for command: {}, rank: {}, suit: {}".format(card_cmd_str, rank, suit))
        
        return cls(int(rank), suit)

    @staticmethod
    def _get_rank_from_user_cmd(rank_str):
        '''Converts any letter representation of a card rank into a numerical representation.'''

        if rank_str in CARD_VALS.values():
            return str(list(CARD_VALS.values()).index(rank_str))
        else:
            return rank_str

    def in_list(self, lst):
        '''Check if card is in given list.'''
        
        for lst_card in lst:
            rank_match = lst_card.rank == self.rank
            suit_match = lst_card.suit == self.suit
            if rank_match and suit_match:
                return True
        else:
            return False
    
    def remove_from_list(self, lst):
        '''Removes card from given list'''

        for i, lst_card in enumerate(lst):
            rank_match = lst_card.rank == self.rank
            suit_match = lst_card.suit == self.suit
            if rank_match and suit_match:
                return lst.pop(i)
        else:
            return lst


class Deck(object):
    '''Represents a deck of playing cards'''

    def __init__(self, deck_num=1):
        '''Creates game_deck dependent of number of decks used.'''

        self.cards = [Card(r,s) for s in SUITS for r in RANKS] * deck_num

    def shuffle(self):
        '''Shuffles the cards.'''

        random.shuffle(self.cards)
    
    def deal(self, players):
        '''Deals cards to provides Players instance'''

        for i, player in enumerate(players):
            player.hand = self.cards[i::len(players)]
