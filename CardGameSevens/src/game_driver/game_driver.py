'''
Created on 11 Jun 2020

@author: Christopher Brett
'''
from game_state.game_state import GameState
from cli.cli_functions import Cli
from colorama.initialise import init


class GameDriver(object):
    '''This class creates a game_state object and runs the game logic above this level'''

    def __init__(self):
        '''Declares cli class and initialises coloured fonts.'''

        self.cli = Cli()
        init()

    def create(self):
        '''Creates game state from user input and runs the game until the rounds are concluded.'''

        # Create Game State based on user input for game parameters
        self.game = GameState(self.cli.create_game())

        # Run the game until a player has won
        while self.game.check_game_end() == False:
            print("Game Start")
            self.run_game()

    def run_game(self):
        '''Runs the rounds and starts new rounds if a player is identified as a winner.'''

        # Call run_round until there is a winner
        while self.game.check_round_winner() == False:
            print("Round Start")
            self.run_round()

        # Start a new round
        self.game.start_new_round()

    def run_round(self):
        '''Handles the running of a turn, print to cli and requesting user input.'''

        # Display current game state in cli output
        self.game.print_round_state_to_cli()

        # Process command from current_player
        self.game.process_command()
        
        # Check if this was a winning move
        if self.game.check_round_winner():
            print("Player '{}' is the Winner!".format(self.game.current_player))
        else:
            self.game.end_turn()
