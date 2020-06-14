'''
Created on 11 Jun 2020

@author: Christopher Brett
'''

from players.human import Human
from players.computer import Computer


class Players(object):
    '''Provides methods for operating on a list of Player instances'''

    def __init__(self, player_num, human_num, comp_levels):
        '''Creates Human and computer players based on user input for game creation.'''

        # Create Human and Computer players accordingly
        self.players = [
            Human(i) if i < human_num else Computer(i, comp_levels[i])
            for i in range(player_num)
            ]

    def __len__(self):
        return len(self.players)

    def __getitem__(self, item):
        return self.players[item]

    def clear_hands(self):
        '''Clears all players hands'''

        # Call the "clear_hands" method on each player instance
        map(lambda x: x.clear_hand(), self.players)

    def get_player_by_id(self, get_id):
        '''Returns player instance by id'''

        # Return matching player instance
        for player in self.players:
            if player.player_id == get_id:
                return player
        else:
            return None
