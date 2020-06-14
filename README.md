# CardGameSevens

Sevens is a cli-based card game. Rules can be found at https://www.wikihow.com/Play-Sevens-(Card-Game)

## Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install any missing dependencies.

```bash
pip install colorama
pip install PrettyTable
pip install windows-curses (or equivalent)
```

## Usage

The card game can be started in the terminal with the command: 
```bash
python sevens.py --create
```

The save and load game functionality is not currently implemented.

Further tests will be submitted in the future to debug the following known problems:
* Command line interface robustness
* Computer move selection errors
