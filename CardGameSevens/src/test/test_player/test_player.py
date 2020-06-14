'''
Created on 14 Jun 2020

@author: Chris
'''
import unittest
from players.player import Player
from deck.deck import Deck


class TestPlayer(unittest.TestCase):


    def test_player(self):     
        '''
        '''
        deck = Deck(1)
        player_1 = Player(0)
        player_2 = Player(1)
        
        players = [player_1, player_2]
        
        deck.shuffle()
        deck.deal(players)

        self.assertEqual(len(player_1.hand), 26)
    
    def test_doubledeck(self):
        '''
        '''
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