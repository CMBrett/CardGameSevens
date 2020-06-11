#!/usr/bin/env

import argparse
from cli.cli_functions import Cli

def main():
    '''
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', dest='create', action='store_true', help='Creates a new game')
    parser.add_argument('--load', dest='load', action='store_true', help='Loads a previously saved game')
    parser.add_argument('--list', dest='list', action='store_true', help='lists previously saved games')
    args = parser.parse_args()

    cli = Cli()
    cli.info("Welcome to the Sevens card game!")

    # Determine which function to start the game/display save data
    if args.create:
        input = cli.create_game()
    if args.load:
        cli.load_game()
    if args.list:
        cli.list_saved_games()

    
               

if __name__ == '__main__':
    main()