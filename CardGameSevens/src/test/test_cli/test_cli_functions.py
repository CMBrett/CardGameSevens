'''
Created on 11 Jun 2020

@author: Chris
'''
import unittest
from cli.cli_functions import Cli 

class TestCliFunctions(unittest.TestCase):
    '''
    '''

    def test_cli_create(self):
        inputs = Cli().create_game()
        print(inputs)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCliFunctions']
    unittest.main()