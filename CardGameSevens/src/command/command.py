'''
Created on 11 Jun 2020

@author: Chris
'''

class Command(object):
    '''
    classdocs
    '''


    def __init__(self, card, layout):
        '''
        Constructor
        '''
        self.card = None
        self.layout = None
    
    def get_user_command(self):
        '''
        '''
        pass

    def is_valid(self):
        '''
        '''
        if self.card in self.layout.valid_cards:
            return True
        else:
            return False