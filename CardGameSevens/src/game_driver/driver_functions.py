'''
Created on 11 Jun 2020

@author: Chris
'''
from game_state.game_state import GameState


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
        self.state = self.INIT

    def create(self, deck_num, player_num, human_num, comp_levels):
        '''
        '''
        # Update GameDriver state
        self.state = self.CREATING

        # Create Game State
        self.game = GameState(deck_num, player_num, human_num, comp_levels)

        # Update GameDriver state
        self.state = self.CREATED

    def run(self):
        '''
        '''
        # Display current game state in cli output
        self.game.print_state_to_cli()

        # Process command from current_player
        self.game.process_command()
        
        # Check if this was a winning move
        if self.game.check_winner():
            # TODO: method for ending game
            print("Player '{}' is the Winner of this Round!".format(self.game.current_player))
        else:
            self.game.end_turn()
