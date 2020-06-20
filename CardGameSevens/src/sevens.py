#!/usr/bin/env
'''
Created on 11 Jun 2020

@author: Christopher Brett
'''

import argparse
from game_driver.game_driver import GameDriver

FEATURE_NOT_IMPLEMENTED = "This feature has not been implemented yet"


def main():
    '''Provides Argparser interface to command the game driver'''

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--create', dest='create',
        action='store_true', help='Creates a new game')
    parser.add_argument(
        '--load', dest='load',
        action='store_true', help='Loads a previously saved game'
        )
    parser.add_argument(
        '--list', dest='list',
        action='store_true', help='lists previously saved games'
        )
    args = parser.parse_args()

    # Instantiate game driver
    driver = GameDriver()

    # Determine which function to start the game/display save data
    if args.create:
        driver.create()
    if args.load:
        print(FEATURE_NOT_IMPLEMENTED)
        # TODO: implement load game functionality
#         driver.load_game()
    if args.list:
        print(FEATURE_NOT_IMPLEMENTED)
        # TODO: implement list saved game functionality
#         driver.list_saved_games()


if __name__ == '__main__':
    main()
