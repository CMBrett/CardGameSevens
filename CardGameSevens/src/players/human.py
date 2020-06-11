'''
Created on 9 Jun 2020

@author: Chris
'''
from players.player import Player
from command.command import Command

class Human(Player):
    '''
    classdocs
    '''

    def request_command(self):

        self.current_command = Command().get_user_command()
        
        if self.current_command.is_possible():
            return self.current_command
        else:
            self.request_command()