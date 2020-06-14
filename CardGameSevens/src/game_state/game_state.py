'''
Created on 11 Jun 2020

@author: Christopher Brett
'''

from deck.deck import Deck
from players.players import Players
from layout.layout import Layouts
from players.human import Human

class GameState(object):
    '''The Game State object contains all variables needed to represent a game.'''

    def __init__(self, user_input):
        '''Creates GameState according to user_input'''
        
        # Set starting values for class members
        self.layouts = []
        self.round_number = 0
        self.dealer_id = 0
        self.current_player = 0

        # Set class members based on user input
        self.total_rounds = user_input["rounds"]
        self.deck_num = user_input["decks"]
        self.players = Players(
            user_input["players"],
            user_input["human players"],
            user_input["comp_levels"]
            )
    
    def start_new_round(self):
        '''Updates class variable to start a new round.'''

        # Increment round number
        self.round_number += 1
        
        # Clear players cards
        self.players.clear_hands()

        # Create deck
        self.game_deck = Deck(self.deck_num)

        # Shuffle deck
        self.game_deck.shuffle()

        # Increment dealer_id
        self.dealer_id += 1

        # Deal deck to players
        self.game_deck.deal(self.players)
        
        # Create layouts
        self.layouts = Layouts(self.deck_num)
    
    def process_command(self):
        '''Requests command from current player and updates the class variables.'''

        # Get player instance from the id in the GameState
        current_player_obj = self.players.get_player_by_id(self.current_player)
        
        # Request and validate command from the current player
        self.current_command = current_player_obj.request_command(self.layouts)

        # Update game state with validated command
        self.update()
    
    def update(self):
        '''Updates the players cards, layouts and ends the current player's turn'''

        # Remove card from current players hand
        self.current_command.card.remove_from_list(self.players.get_player_by_id(self.current_player).hand)
        
        # Add card to Layout
        layout = self.layouts.get_layout_by_id(self.current_command.layout.id)
        layout.cards.append(self.current_command.card)
        
        # Update layout valid_cards
        layout.calculate_valid_cards()
        
        # end_turn
        self.end_turn()
    
    def end_turn(self):
        '''Sets current player to next player_id.'''

        # Change current player
        if self.current_player != len(self.players) - 1:
            self.current_player += 1
        else:
            self.current_player = 0

        print("Player_id set to ", self.current_player)

    def check_game_end(self):
        '''Checks if specified number of game rounds have been exceeded.'''

        # Check if current round is larger than the number of total desired rounds
        if self.round_number > self.total_rounds:
            return True
        else:
            return False

    def check_round_winner(self):
        '''Check if current player has played their last card.'''

        # Get player instance from the id in the GameState
        current_player_obj = self.players.get_player_by_id(self.current_player)

        # Return whether player just played winning move
        return current_player_obj.check_if_winner()

    def print_round_state_to_cli(self):
        '''Prints the current layout state and human player's hand if current player'''

        # Print layouts table
        print(self.layouts)
        print("")

        # Get current Player from current_player_id
        current_player_obj = self.players.get_player_by_id(self.current_player)

        # Print Player cards if human
        if isinstance(current_player_obj, Human):
            print("Printing Human Player {} cards:".format(current_player_obj.player_id))
            print(current_player_obj.get_hand_table())
            print("")
