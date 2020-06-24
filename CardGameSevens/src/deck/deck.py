'''
Created on 9 Jun 2020

@author: Christopher Brett
'''

import random
from curses.ascii import isalpha

SUITS = ["C", "D", "H", "S"]
RANKS = list(range(2, 15))
CARD_VALS = {11: "J", 12: "Q", 13: "K", 14: "A"}
FACE_VALS = {"J": 11, "Q": 12, "K": 13, "A": 14}


class Card():
    '''Represents a playing card'''

    def __init__(self, rank, suit):
        '''Creates Card instance from given rank and suit'''

        # Create named tuple instance
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        '''Returns a printable representation of the object'''

        return "({}, {})".format(str(self.rank), str(self.suit))

    def __eq__(self, other):
        '''Defines object equality.'''

        rank_match = self.rank == other.rank
        suit_match = self.suit == other.suit

        return rank_match and suit_match

    @classmethod
    def create_from_user_cmd(cls, card_cmd_str):
        '''Creates a card instance based on user input string'''

        # Determine rank if rank is double digit
        if len(card_cmd_str) == 3:
            rank = card_cmd_str[0:2]
            suit = card_cmd_str[2]
        else:
            if isalpha(card_cmd_str[0]):
                rank = FACE_VALS[card_cmd_str[0]]
                print(rank)
            else:
                rank = card_cmd_str[0]
            suit = card_cmd_str[1]

        return cls(int(rank), suit)

    @staticmethod
    def _get_rank_from_user_cmd(rank_str):
        '''
        Converts any letter representation of a card rank
        into a numerical representation.
        '''

        if rank_str in CARD_VALS.values():
            rank_str = str(list(CARD_VALS.values()).index(rank_str))
        return rank_str

    def remove_from_list(self, lst):
        '''Removes card from given list'''

        for i, lst_card in enumerate(lst):
            rank_match = lst_card.rank == self.rank
            suit_match = lst_card.suit == self.suit
            if rank_match and suit_match:
                lst.pop(i)
        return lst


class Deck():
    '''Represents a deck of playing cards'''

    def __init__(self, deck_num=1):
        '''Creates game_deck dependent of number of decks used.'''

        self.__i = 0
        self.cards = [Card(r, s) for s in SUITS for r in RANKS] * deck_num

    def __iter__(self):
        self.__i = 0
        return iter(self.cards)

    def shuffle(self):
        '''Shuffles the cards.'''

        random.shuffle(self.cards)

    def deal(self, players):
        '''Deals cards to provides Players instance'''

        for i, player in enumerate(players):
            player.hand = self.cards[i::len(players)]
