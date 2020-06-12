'''
Created on 11 Jun 2020

@author: Chris
'''
from builtins import int
from colorama import Fore
from colorama.initialise import init

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
        self.current_input = None
        self.instruction = None
        self.input = {}
        init()

    def create_game(self):
        '''
        '''
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

        if not self.check_input_type():
            print("Invalid input: Please enter a value for {} as an integer.")
            self.request_user_input()
        else:
            self.store_user_input()

    def check_input_type(self):
        '''
        '''
        try:
            self.proc_input = Instructions.DATA_TYPE[self.instruction](self.current_input)
        except Exception:
            return False
        else:
            return True
    
    def check_input_value(self):
        '''
        '''
        
    
    def store_user_input(self):
        '''
        '''
        self.input[self.instruction] = self.proc_input
    
    def info(self, output_str):
        '''
        '''
        init()
        print(Fore.BLUE + output_str + Fore.RESET)
    
    def request_input(self, output_str):
        '''
        '''
        print(Fore.MAGENTA + output_str + Fore.RESET)
    
    def warning(self, output_str):
        '''
        '''
        print(Fore.YELLOW + output_str + Fore.RESET)
        
    def error(self, output_str):
        '''
        '''
        print(Fore.RED + output_str + Fore.RESET)
    
    def notice(self, output_str):
        '''
        '''
        print(output_str)
