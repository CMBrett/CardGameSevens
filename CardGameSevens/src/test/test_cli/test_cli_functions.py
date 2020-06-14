'''
Created on 11 Jun 2020

@author: Christopher Brett
'''
import unittest
from cli.cli_functions import Cli 

class TestCliFunctions(unittest.TestCase):
    '''This test class is for testing the cli_functionality in cli.cli_functions.'''

    def test_cli_create(self):
        '''This test ensures that the cli.create_game function does not raise any exceptions.'''
        
        output = Cli().create_game()
        # TODO: add mock user input
        
        print(output)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCliFunctions']
    unittest.main()