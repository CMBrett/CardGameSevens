'''
Created on 14 Jun 2020

@author: Chris
'''
import unittest
from players.player import Player
from deck.deck import Deck


class TestPlayer(unittest.TestCase):
    '''This test class tests the functionality within the players package'''

    def test_player(self):     
        '''Ensures that both players have 26 cards in their hand after dealing 1 deck.'''

        deck = Deck(1)
        player_1 = Player(0)
        player_2 = Player(1)
        
        players = [player_1, player_2]
        
        deck.shuffle()
        deck.deal(players)

        self.assertEqual(len(player_1.hand), 26)
    
    def test_doubledeck(self):
        '''Ensures that both players have 52 cards in their hand after dealing 2 decks.'''

        deck = Deck(2)
        player_1 = Player(0)
        player_2 = Player(1)

        players = [player_1, player_2]

        deck.shuffle()
        deck.deal(players)

        self.assertEqual(len(player_1.hand), 52)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
