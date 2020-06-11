'''
Created on 9 Jun 2020

@author: Chris
'''
import collections

SUITS = ["clubs", "diamonds", "hearts", "spades"]
RANKS = [n for n in range(2, 14)]


Card = collections.namedtuple("Card", ["rank", "suit"])

class Deck(object):
    '''
    classdocs
    '''

    def __init__(self, deck_num=1):
        '''
        Constructor
        '''
        self.cards = [Card(r,s) for s in SUITS for r in RANKS] * deck_num
                
        