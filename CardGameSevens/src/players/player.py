'''
Created on 9 Jun 2020

@author: Christopher Brett
'''
from prettytable import PrettyTable
from deck.deck import SUITS, CARD_VALS
from utility import utility


class Player():
    '''Parent class of Human and Computer players, contains common methods'''

    def __init__(self, player_id):
        '''Creates Player instance based on player_id'''

        self.player_id = player_id
        self.hand = []
        self.rounds_won = 0
        self.current_command = None
        self.current_layouts = []

    def clear_hand(self):
        '''Removes all cards from a player's hand'''

        self.hand = []

    def sort_hand(self):
        '''Sorts hand based on rank'''

        self.hand = sorted(self.hand, key=lambda h: h.rank)

    def check_if_winner(self):
        '''Checks if player's hand is empty'''

        return bool(len(self.hand) == 0)

    def __str__(self):
        player_string = []
        newline = "\n"

        player_string.append("Player: '{}'".format(self.player_id))
        player_string.append(newline)
        player_string.append("Rounds won: '{}'".format(self.rounds_won))
        player_string.append(newline)
        player_string.append("Current Cards: '{}'".format(self.hand))
        player_string.append(newline)

        for card in self.hand:
            player_string.append(card)
            player_string.append(newline)

        return ", ".join(player_string)

    def get_hand_table(self):
        '''Provides table string for printing current cards in player's hand to cli'''

        # Create table and add headers
        table = PrettyTable()

        # Add data of each layout to the table
        clubs_col = self.card_val(
            sorted([c.rank for c in self.hand if c.suit == "C"])
            )
        diamo_col = self.card_val(
            sorted([c.rank for c in self.hand if c.suit == "D"])
            )
        heart_col = self.card_val(
            sorted([c.rank for c in self.hand if c.suit == "H"])
            )
        spade_col = self.card_val(
            sorted([c.rank for c in self.hand if c.suit == "S"])
            )
        columns = [clubs_col, diamo_col, heart_col, spade_col]

        longest_list_length = len(max(columns, key=len))

        for i, col in enumerate(columns):
            if len(col) < longest_list_length:
                columns[i] = utility.pad(col, "", longest_list_length)
            table.add_column(SUITS[i], columns[i], align='c', valign='m')
        return table.get_string()

    @staticmethod
    def card_val(ranks):
        '''Replaces text representation for face cards with integer'''

        for i, rank in enumerate(ranks):
            if rank > 10:
                ranks[i] = CARD_VALS[rank]

        return ranks
