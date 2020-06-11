import argparse
from cli.cli_functions import create_game, load_game, list_saved_games

def main():
    '''
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', dest='create', action='store_true', help='Creates a new game')
    parser.add_argument('--load', dest='load', action='store_true', help='Loads a previously saved game')
    parser.add_argument('--list', dest='list', action='store_true', help='lists previously saved games')
    args = parser.parse_args()

    # Determine which function to start the game/display save data
    if args.create:
        create_game()
    if args.load:
        load_game()
    if args.list:
        list_saved_games()