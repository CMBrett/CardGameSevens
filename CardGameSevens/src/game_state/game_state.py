'''
Created on 11 Jun 2020

@author: Chris
'''
from deck.deck import Deck
from players.human import Human
from players.computer import Computer

class GameState(object):
    '''
    classdocs
    '''


    def __init__(self, deck_num, player_num, human_num, comp_levels):
        '''
        Constructor
        '''
        # Create Players
        self.players = []
        self.dealer_id = 0
        self.current_player = 0
        
        for i in range(1, player_num):
            if i < human_num:
                self.players.append(Human(i))
            else:
                self.players.append(Computer(i, comp_levels[i]))
        
        # Create deck
        self.game_deck = Deck(deck_num)
        
        # Shuffle deck
        self.game_deck.shuffle()
        
        # Deal deck to dlayers
        self.game_deck.deal()
    
    def process_command(self):
        '''
        '''
        self.current_command = self.current_player.request_command()
        self.update(self.current_command)
    
    def end_turn(self):
        '''
        '''
        # TODO: change current player
    
    def check_winner(self):
        '''
        '''
        return self.current_player.check_if_winner()
    
    
    
    def print_state_to_cli(self):
        '''
        '''
        pass