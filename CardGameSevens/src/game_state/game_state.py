'''
Created on 11 Jun 2020

@author: Chris
'''

from deck.deck import Deck
from players.players import Players
from layout.layout import Layouts
from players.human import Human

class GameState(object):
    '''
    classdocs
    '''


    def __init__(self, user_input):
        '''
        Constructor
        '''
        
        self.layouts = []
        self.round_number = 0
        self.total_rounds = user_input["rounds"]
        self.dealer_id = 0
        self.current_player = 0
        self.deck_num = user_input["decks"]
        
        self.players = Players(
            user_input["players"],
            user_input["human players"],
            user_input["comp_levels"]
            )
    
    def start_new_round(self):
        '''
        '''

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
        '''
        '''

        # Get player instance from the id in the GameState
        current_player_obj = self.players.get_player_by_id(self.current_player)
        
        # Request and validate command from the current player
        self.current_command = current_player_obj.request_command(self.layouts)

        # Update game state with validated command
        self.update()
    
    def update(self):
        '''
        '''
        # Remove card from current players hand
        self.current_command.card.remove_from_list(self.players.get_player_by_id(self.current_player).hand)
        
        # Add card to Layout
        layout = self.layouts.get_layout_by_suit(self.current_command.card.suit)
        layout.cards.append(self.current_command.card)
        
        # Update layout valid_cards
        layout.calculate_valid_cards()
        
        # end_turn
        self.end_turn()
    
    def end_turn(self):
        '''
        '''
        # Change current player
        if self.current_player != len(self.players) - 1:
            self.current_player += 1
        else:
            self.current_player = 0
        
        print("Player_id set to ", self.current_player)
        
    
    def check_game_end(self):
        '''
        '''
        # TODO: multiple round game-winning logic
        if self.round_number > self.total_rounds:
            return True
        else:
            return False
    
    def check_round_winner(self):
        '''
        '''
        # Get player instance from the id in the GameState
        current_player_obj = self.players.get_player_by_id(self.current_player)

        # Return whether player just played winning move
        return current_player_obj.check_if_winner()
    
    def print_round_state_to_cli(self):
        '''
        '''
        
        # Print layouts table
        print(self.layouts)
        print("")

        # Print Player cards if human
        current_player_obj = self.players.get_player_by_id(self.current_player)
        
        if isinstance(current_player_obj, Human):
            print("Printing Human Player {} cards:".format(current_player_obj.player_id))
            print(current_player_obj.get_hand_table())
            print("")

