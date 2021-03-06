'''
Created on 11 Jun 2020

@author: Christopher Brett
'''

from colorama import Fore
from colorama.initialise import init


def get_input():
    '''Returns the user input command from the CLI
    '''

    return input()


class Instructions():
    '''
    Contains output strings to prompt user input
    and default and type for checking input.
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
    VALUE = {
        DECK_NUM: (1, 3),
        ROUND_NUM: (1, 3),
        PLAYER_NUM: (1, 3),
        HUMAN_NUM: (1, 3),
        COMP_LEVEL: (1, 2)
    }

    INSTRUCTION_STR = "Please enter an integer to determine the number of {} \
    for this game: (default={}, min={}, max={})"
    COMP_LEVEL_STR = "Please enter an integer to determine the {} for \
    'Computer {}' for this game: (default={}, min=1, max=2)"

    # Instruction for variable entry to be printed to CLI
    INSTRUCTION = {
        DECK_NUM: INSTRUCTION_STR.format(
            DECK_NUM, DEFAULT[DECK_NUM],
            VALUE[DECK_NUM][0], VALUE[DECK_NUM][1]
        ),
        ROUND_NUM: INSTRUCTION_STR.format(
            ROUND_NUM, DEFAULT[ROUND_NUM],
            VALUE[ROUND_NUM][0], VALUE[ROUND_NUM][1]
        ),
        PLAYER_NUM: INSTRUCTION_STR.format(
            PLAYER_NUM, DEFAULT[PLAYER_NUM],
            VALUE[PLAYER_NUM][0], VALUE[PLAYER_NUM][1]
        ),
        HUMAN_NUM: INSTRUCTION_STR.format(
            HUMAN_NUM, DEFAULT[HUMAN_NUM],
            VALUE[HUMAN_NUM][0], VALUE[HUMAN_NUM][1]
        ),
    }

    # Instructions to request when creating a game
    CREATE = [DECK_NUM, ROUND_NUM, PLAYER_NUM, HUMAN_NUM]

    # Instructions to request when loading a game
    LOAD = [LOAD_ID]


class Cli():
    '''
    Cli is used to request and check user input
    and output coloured commands to the cli.
    '''

    def __init__(self):
        '''Declares class members for use in member functions'''

        self.current_input = None
        self.instruction = None
        self.input = {}

        self.player_num = 0
        self.human_num = 0

        self.comp_instr_str = []
        self.proc_input = None

        self.value_dict = {
            Instructions.DECK_NUM: (1, 3),
            Instructions.ROUND_NUM: (1, 3),
            Instructions.PLAYER_NUM: (1, 8),
            Instructions.HUMAN_NUM: (1, self.player_num)
        }

        init()

    def create_game(self):
        '''Requests user input for game creation parameters.'''

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

    def load_game(self):
        '''Requests user input for game load parameters.'''

        raise NotImplementedError

    def list_saved_games(self):
        '''Lists all saved games.'''

        raise NotImplementedError

    def request_user_input(self):
        '''
        Requests user input and checks type and value,
        requests input again if checks are unsuccessful.
        '''

        # Insert new line in output for clarity
        self.info("")

        # Print instruction and retrieve user input
        self.request_input(Instructions.INSTRUCTION[self.instruction])
        self.current_input = get_input()

        if self.current_input == "":
            self.current_input = Instructions.DEFAULT[self.instruction]
            self.info(
                "'{}' set to default value: '{}'".format(
                    self.instruction, self.current_input
                    )
                )

        # Store input if type + value check are successful else rerequest input
        if self.check_input_type() and self.check_input_value():
            self.store_user_input()
        else:
            self.error(
                "Invalid input: Please enter a value for {} \
                as an integer.".format(self.instruction)
            )
            self.request_user_input()

    def request_comp_levels(self, comp_id):
        '''Requests user input for computer difficulty levels.'''

        # Insert new line in output for clarity
        self.info("")

        # Print appropriate instruction string
        self.request_input(
            Instructions.COMP_LEVEL_STR.format(
                Instructions.COMP_LEVEL, comp_id,
                Instructions.DEFAULT[Instructions.COMP_LEVEL],
                Instructions.VALUE[Instructions.COMP_LEVEL][0],
                Instructions.VALUE[Instructions.COMP_LEVEL][1]
            )
        )

        # Await user input
        self.current_input = input()

        # Apply default parameter
        if self.current_input == "":
            self.current_input = Instructions.DEFAULT[Instructions.COMP_LEVEL]
            self.info("'{}' set to default value: '{}'".format(
                self.instruction, self.current_input
            ))

        # Create dict entry in input dict for the computer levels
        self.input["comp_levels"] = {}

        # Store input if type + value check are successful else rerequest input
        if self.check_input_type() or self.check_input_value():
            self.store_user_input(comp_id)
        else:
            self.error("Invalid input: Please enter a value for {} \
            as an integer.".format(self.instruction))
            self.request_comp_levels(comp_id)

    def generate_comp_instr_str(self):
        '''
        Generates instruction strings to prompt user for
        computer difficulty level.
        '''

        # Calculate number of computer players
        computer_num = self.player_num - self.human_num

        # Calculate strating number for computer player_ids
        starting_com_index = self.human_num + 1

        # Create list of instruction strings for user input
        self.comp_instr_str = [
            Instructions.COMP_LEVEL_STR.format(
                Instructions.COMP_LEVEL, i,
                Instructions.DEFAULT[Instructions.COMP_LEVEL],
                Instructions.VALUE[Instructions.COMP_LEVEL][0],
                Instructions.VALUE[Instructions.COMP_LEVEL][1]
            )
            for i in range(
                starting_com_index, starting_com_index + computer_num
            )
        ]

    def check_input_type(self):
        '''Checks string input can be cast to correct data type.'''

        try:
            # Check provided input can be cast to intended data type
            self.proc_input = Instructions.DATA_TYPE[self.instruction](
                self.current_input
            )
        except ValueError:
            return False
        else:
            return True

    def check_input_value(self):
        '''Checks value of given input is acceptable.'''

        value_def = Instructions.VALUE[self.instruction]

        try:
            # Raise exceptions if provided value is unacceptable as input
            if self.proc_input < value_def[0]:
                raise ValueError("Input is smaller than the minimum limit")

            if self.proc_input > value_def[1]:
                raise ValueError("Input is larger than the maximum limit")

        except ValueError as exc:
            print(exc)
            return False
        else:
            return True

    def store_user_input(self, comp_id=None):
        '''
        Stores user input to dict which will be used to create the game_state
        '''

        if comp_id is None:
            # Add processed input to input dict using the instruction as the
            # key
            self.input[self.instruction] = self.proc_input
        else:
            # Add processed input to comp_levels entry of input dict
            self.input["comp_levels"][comp_id +
                                      self.human_num] = self.proc_input

    @staticmethod
    def info(output_str):
        '''Prints info message to cli in light blue.'''

        print(Fore.LIGHTBLUE_EX + output_str + Fore.RESET)

    @staticmethod
    def request_input(output_str):
        '''Prints user prompt to cli in magenta.'''

        print(Fore.MAGENTA + output_str + Fore.RESET)

    @staticmethod
    def warning(output_str):
        '''Prints warning message to cli in yellow.'''

        print(Fore.YELLOW + output_str + Fore.RESET)

    @staticmethod
    def error(output_str):
        '''Prints error message to cli in red.'''

        print(Fore.RED + output_str + Fore.RESET)

    @staticmethod
    def notice(output_str):
        '''Prints notice message to cli in default colour.'''

        print(output_str)
