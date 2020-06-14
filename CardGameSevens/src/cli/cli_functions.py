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
    ROUND_NUM = "rounds"
    PLAYER_NUM = "players"
    HUMAN_NUM = "human players"
    COMP_LEVEL = "computer difficulty level"
    LOAD_ID = "load_id"
    
    # Data type for each possible instruction
    DATA_TYPE = {
        DECK_NUM: int,
        ROUND_NUM: int,
        PLAYER_NUM: int,
        HUMAN_NUM: int,
        COMP_LEVEL: int
        }

    # Default_value for each possible instruction
    DEFAULT = {
        DECK_NUM: 1,
        ROUND_NUM: 1,
        PLAYER_NUM: 2,
        HUMAN_NUM: 1,
        COMP_LEVEL: 1
        }
    
    # Min and Max Value for each input parameter
    # TODO: create Namedtuple ValueDef
    VALUE = {
        DECK_NUM: (1,3),
        ROUND_NUM: (1,3),
        PLAYER_NUM: (1,3),
        HUMAN_NUM: (1,3),
        COMP_LEVEL: (1,2)
        }
    
    INSTRUCTION_STR = "Please enter an integer to determine the number of {} for this game: (default={}, min={}, max={})"
    COMP_LEVEL_STR = "Please enter an integer to determine the {} for 'Computer {}' for this game: (default={}, min=1, max=2)"
    
    # Instruction for variable entry to be printed to CLI
    INSTRUCTION= {
        DECK_NUM: INSTRUCTION_STR.format(DECK_NUM, DEFAULT[DECK_NUM], VALUE[DECK_NUM][0], VALUE[DECK_NUM][1]),
        ROUND_NUM: INSTRUCTION_STR.format(ROUND_NUM, DEFAULT[ROUND_NUM], VALUE[ROUND_NUM][0], VALUE[ROUND_NUM][1]),
        PLAYER_NUM: INSTRUCTION_STR.format(PLAYER_NUM, DEFAULT[PLAYER_NUM], VALUE[PLAYER_NUM][0], VALUE[PLAYER_NUM][1]),
        HUMAN_NUM: INSTRUCTION_STR.format(HUMAN_NUM, DEFAULT[HUMAN_NUM], VALUE[HUMAN_NUM][0], VALUE[HUMAN_NUM][1]),
        }
    
    # Instructions to request when creating a game
    CREATE = [DECK_NUM, ROUND_NUM, PLAYER_NUM, HUMAN_NUM]

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

        self.player_num = 0

        self.value_dict = {
            Instructions.DECK_NUM: (1, 3),
            Instructions.ROUND_NUM: (1, 3),
            Instructions.PLAYER_NUM: (1, 8),
            Instructions.HUMAN_NUM: (1, self.player_num)
            }

        init()

    def create_game(self):
        '''
        '''

        # Request necessary parameters
        for instr in Instructions.CREATE:
            self.instruction = instr
            self.request_user_input()
        
        # Assign members to allow request of computer Levels
        self.player_num = self.input[Instructions.PLAYER_NUM]
        self.human_num = self.input[Instructions.HUMAN_NUM]
        self.generate_comp_instr_str()

        # Request comp level for each computer player
        for i, instr in enumerate(self.comp_instr_str):
            # Request necessary parameters
            self.instruction = Instructions.COMP_LEVEL
            self.request_comp_levels(i)

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

        # Print instruction and retrieve user input
        self.info(Instructions.INSTRUCTION[self.instruction])
        self.current_input = input()

        # Store input if type and value check are successful, else request new input
        if self.check_input_type() and self.check_input_value():
            self.store_user_input()
        else:
            self.error("Invalid input: Please enter a value for {} as an integer.".format(self.instruction))
            self.request_user_input()
    
    def request_comp_levels(self, comp_id):
        '''
        '''

        self.info(
            Instructions.COMP_LEVEL_STR.format(
                Instructions.COMP_LEVEL, comp_id, Instructions.DEFAULT[Instructions.COMP_LEVEL],
                    Instructions.VALUE[Instructions.COMP_LEVEL][0], Instructions.VALUE[Instructions.COMP_LEVEL][1]
                    )
            )
        self.current_input = input()

        # Create dict entry in input dict for the computer levels
        self.input["comp_levels"] = {}

        # Store input if type and value check are successful, else request new input
        if self.check_input_type() or self.check_input_value():
            self.store_user_input(comp_id)
        else:
            self.error("Invalid input: Please enter a value for {} as an integer.".format(self.instruction))
            self.request_comp_levels()
    
    def generate_comp_instr_str(self):
        '''
        '''

        computer_num = self.player_num - self.human_num
        starting_com_index = self.human_num + 1
        self.comp_instr_str = [
            Instructions.COMP_LEVEL_STR.format(
                    Instructions.COMP_LEVEL, i, Instructions.DEFAULT[Instructions.COMP_LEVEL],
                    Instructions.VALUE[Instructions.COMP_LEVEL][0], Instructions.VALUE[Instructions.COMP_LEVEL][1])
            for i in range(starting_com_index, starting_com_index + computer_num)
            ]

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

        value_def = Instructions.VALUE[self.instruction]
        
        try:
            # TODO: create cli message to inform user of value violation type
            if self.proc_input < value_def[0]:
                raise ValueError("Input is smaller than the minimum limit")
            
            if self.proc_input > value_def[1]:
                raise ValueError("Input is larger than the maximum limit")
            
        except Exception as exc:
            print(exc)
            return False
        else:
            return True

    def store_user_input(self, comp_id=None):
        '''
        '''
        if comp_id is None:
            self.input[self.instruction] = self.proc_input
        else:
            
            self.input["comp_levels"][comp_id + self.human_num] = self.proc_input

    def info(self, output_str):
        '''
        '''
        print(Fore.LIGHTBLUE_EX + output_str + Fore.RESET)
    
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
