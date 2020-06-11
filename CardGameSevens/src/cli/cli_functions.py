'''
Created on 11 Jun 2020

@author: Chris
'''
from builtins import int

class Instructions(object):
    '''
    '''
    DECK_NUM = "decks"
    PLAYER_NUM = "players"
    HUMAN_NUM = "human players"
    LOAD_ID = "load_id"
    
    # Instruction for variable entry to be printed to CLI
    INSTRUCTION= {
        DECK_NUM: "Please enter an integer to represent the number of {} for this game: (default=1)\n",
        PLAYER_NUM: "Please enter an integer to represent the number of {} for this game: (default=1)\n",
        HUMAN_NUM: "Please enter an integer to represent the number of {} for this game: (default=1)\n"
        }
    
    # Data type for each possible instruction
    DATA_TYPE = {
        DECK_NUM: int,
        PLAYER_NUM: int,
        HUMAN_NUM: int
        }
    
    # Instructions to request when creating a game
    CREATE = [DECK_NUM, PLAYER_NUM, HUMAN_NUM]

    # Instructions to request when loading a game
    LOAD = [LOAD_ID]
    

class Cli(object):
    '''
    classdocs
    '''

    def __init__(self):
        print("Initialising CLI class")
        self.current_input = None
        self.instruction = None
        self.input = {}

    def create_game(self):
        '''
        '''
        print("Creating new game via CLI")
        
        for instr in Instructions.CREATE:
            # Request necessary parameters
            self.instruction = instr
            self.request_user_input()
        
        # TODO: Request Computer Levels

        return self.input

    @staticmethod
    def load_game(self):
        '''
        '''
        pass

    @staticmethod
    def list_saved_games(self):
        '''
        '''
        pass

    def request_user_input(self):
        '''
        '''
        print(Instructions.INSTRUCTION[self.instruction])
        self.current_input = input()

        if not self.check_valid_input():
            print("Invalid input: Please enter a value for {} as an integer.")
            self.request_user_input()
        else:
            self.store_user_input()

    def check_valid_input(self):
        '''
        '''
        try:
            self.proc_input = Instructions.DATA_TYPE[self.instruction](self.current_input)
        except Exception:
            return False
        else:
            return True
    
    def store_user_input(self):
        '''
        '''
        self.input[self.instruction] = self.proc_input
