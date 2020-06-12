'''
Created on 11 Jun 2020

@author: Chris
'''
from game_state.game_state import GameState
from cli.cli_functions import Cli


class GameDriver(object):
    '''
    classdocs
    '''
    INIT = "init"
    CREATING = "creating" 
    CREATED = "created"

    def __init__(self):
        '''
        Constructor
        '''
        self.cli = Cli()

    def create(self, deck_num, player_num, human_num, comp_levels):
        '''
        '''
        # Request user input for game parameters
        user_input = self.cli.create_game()

        # Create Game State
        self.game = GameState(deck_num, player_num, human_num, comp_levels)

        # Run the game until a player has won
        while self.game.check_game_winner() == False:
            self.run_game()

    def run_game(self):
        '''
        '''
        while self.game.check_round_winner() == False:
                self.run_round()
        
        # Start a new round
        self.game.start_new_round()

    def run_round(self):
        '''
        '''
        # Display current game state in cli output
        self.game.print_state_to_cli()

        # Process command from current_player
        self.game.process_command()
        
        # Check if this was a winning move
        if self.game.check_winner():
            # TODO: method for ending game
            print("Player '{}' is the Winner!".format(self.game.current_player))
        else:
            self.game.end_turn()
