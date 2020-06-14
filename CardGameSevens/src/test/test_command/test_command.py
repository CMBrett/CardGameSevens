'''
Created on 14 Jun 2020

@author: Chris
'''
import unittest
from deck.deck import Deck, Card
from players.player import Player
from command.command import Command
from layout.layout import Layouts
from game_state.game_state import GameState

suit_layout_dict = {"C": 0,"D": 1,"H": 2,"S": 3} 

class TestCommand(unittest.TestCase):
    '''This test class tests the functionality within the command package'''

    def test_valid_command(self):
        '''This test ensures that a valid command is correctly checked'''

        deck = Deck(1)
        player_1 = Player(0)
        player_2 = Player(1)

        players = [player_1]
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
    
    def test_card_ten(self):
        '''This test check that a card can be played with a double digit rank'''
       
        test_input = {'decks': 1, 'rounds': 1, 'players': 1, 'human players': 1, 'comp_levels': {}}
        
        state = GameState(test_input)
        
        state.start_new_round()
        
        player_obj = state.players.get_player_by_id(state.current_player)
        
        player_obj.hand = [c for c in Deck(1)]
        
        state.print_round_state_to_cli()

        test_commands = []

        test_commands.append(Command("7CL0", state.layouts))
        test_commands.append(Command("8CL0", state.layouts))
        test_commands.append(Command("9CL0", state.layouts))
        test_commands.append(Command("10CL0", state.layouts))
        test_commands.append(Command("JCL0", state.layouts))
        test_commands.append(Command("QCL0", state.layouts))
        test_commands.append(Command("KCL0", state.layouts))
        test_commands.append(Command("ACL0", state.layouts))
        test_commands.append(Command("6CL0", state.layouts))
        test_commands.append(Command("5CL0", state.layouts))
        test_commands.append(Command("4CL0", state.layouts))
        test_commands.append(Command("3CL0", state.layouts))
        test_commands.append(Command("2CL0", state.layouts))
        
        for test_command in test_commands:
            state.current_command = test_command
            state.update()
        
        state.print_round_state_to_cli()
        
        extra_command = Command("7HL2", state.layouts)
        state.current_command = extra_command
        state.update()
        state.print_round_state_to_cli()

    def test_round_end(self):
        '''This test check that a winner is found'''

        test_input = {'decks': 1, 'rounds': 2, 'players': 1, 'human players': 1, 'comp_levels': {}}
        
        state = GameState(test_input)
        
        state.start_new_round()
        
        player_obj = state.players.get_player_by_id(state.current_player)
        
        player_obj.hand = [c for c in Deck(1)]
        
        state.print_round_state_to_cli()
        
        test_cmd_strs_1 = [
            str(i) + s + "L" + str(suit_layout_dict[s])
            for s in suit_layout_dict.keys() for i in range(7,15)
            ]
        
        test_cmd_strs_2 = [
            str(i) + s + "L" + str(suit_layout_dict[s])
            for s in suit_layout_dict.keys() for i in range(2,7)
            ]
        
        
        test_cmd_strs_2.reverse()
        
        test_cmd_strs = test_cmd_strs_1 + test_cmd_strs_2
        
        print(test_cmd_strs)
        
        test_commands = [Command(c, state.layouts) for c in test_cmd_strs]
        
        player_obj = state.players.get_player_by_id(state.current_player)
        
        while not state.check_round_winner():
            for test_command in test_commands:
                state.current_command = test_command
                state.update()
                state.print_round_state_to_cli()

        state.start_new_round()
        
        self.assertEqual(state.round_number, 2)
        self.assertEqual(state.dealer_id, 0)

        while not state.check_round_winner():
            for test_command in test_commands:
                state.current_command = test_command
                state.update()
                state.print_round_state_to_cli()

        
        print("Total rounds: ", state.total_rounds)
        print("round_number: ", state.round_number)
        self.assertTrue(state.check_game_end())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
