'''
Created on 11 Jun 2020

@author: Chris
'''

from deck.deck import Deck
from players.players import Players
from layout.layout import Layouts

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
        self.game_deck.deal()
        
        # Create layouts
        self.layouts = Layouts(self.deck_num)
    
    def process_command(self):
        '''
        '''
        # Get player instance from the id in the GameState
        current_player_obj = self.players.get_player_by_id(self.current_player)
        
        # Request and validate command from the current player
        self.current_command = current_player_obj.request_command()

        # Update game state with validated command
        self.update(self.current_command)
    
    def update(self):
        '''
        '''
        # Remove card from current players hand
        self.current_player.hand.remove(self.current_command.card)
        
        # Add card to Layout
        self.layouts.get_layout_by_suit(self.current_command.card.suit).cards.append(self.current_command.card)
    
    def end_turn(self):
        '''
        '''
        # TODO: change current player
    
    def check_game_winner(self):
        '''
        '''
        # TODO: multiple round game-winning logic
        return True
    
    def check_round_winner(self):
        '''
        '''
        # Get player instance from the id in the GameState
        current_player_obj = self.players.get_player_by_id(self.current_player)

        # Return whether player just played winning move
        return current_player_obj.check_if_winner()
    
    def print_state_to_cli(self):
        '''
        '''
        pass
