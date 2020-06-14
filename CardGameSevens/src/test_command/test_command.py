'''
Created on 14 Jun 2020

@author: Chris
'''
import unittest
from deck.deck import Deck, Card
from players.player import Player
from command.command import Command
from layout.layout import Layouts


class TestCommand(unittest.TestCase):
    '''This test class tests the functionality within the command package'''

    def test_valid_command(self):
        '''This test ensures that a valid command is correctly checked'''

        deck = Deck(1)
        player_1 = Player(0)
        player_2 = Player(1)

        players = [player_1, player_2]
        layouts = Layouts(1)

        deck.shuffle()
        deck.deal(players)

        seven_suits = [c.suit for c in player_1.hand if c.rank==7]
        test_suit = seven_suits[0]
        card_cmd_str = "7" + test_suit
        
        layout_dict = {
            "C": "L0",
            "D": "L1",
            "H": "L2",
            "S": "L3"
            }
        
        layout_cmd_str = layout_dict[test_suit]
        cmd_str = card_cmd_str + layout_cmd_str

        cmd = Command(cmd_str, layouts)
        self.assertTrue(cmd.is_valid(player_1.hand))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
