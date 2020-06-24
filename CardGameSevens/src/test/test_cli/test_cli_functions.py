'''
Created on 11 Jun 2020

@author: Christopher Brett
'''
import unittest
from cli.cli_functions import Cli


class MockInputFunction:
    def __init__(self, return_value=None):
        self.return_value = return_value
        self._orig_input_fn = __builtins__['input']

    def _mock_input_fn(self):
        print(str(self.return_value))
        return self.return_value

    def __enter__(self):
        __builtins__['input'] = self._mock_input_fn

    def __exit__(self, type, value, traceback):
        __builtins__['input'] = self._orig_input_fn


class TestCliFunctions(unittest.TestCase):
    '''
    This test class is for testing the cli_functionality
    in cli.cli_functions.
    '''

    def test_cli_correct_arguments(self):
        '''
        This test ensures that the cli.create_game
        function does not raise any exceptions.
        '''

        with MockInputFunction(return_value="2"):
            Cli().create_game()

    def test_cli_zero_arguments(self):
        '''
        This test ensures that the cli.create_game function
        does not raise any exceptions.
        '''

        with MockInputFunction(return_value="0"):
            with self.assertRaises(RecursionError):
                Cli().create_game()

    def test_cli_eight_arguments(self):
        '''
        This test ensures that the cli.create_game function
        does not raise any exceptions.
        '''

        with MockInputFunction(return_value="8"):
            with self.assertRaises(RecursionError):
                Cli().create_game()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCliFunctions']
    unittest.main()
