#!/usr/bin/env python3
from brain_games.logic_games import run_game
from brain_games.games.even import find_even_number, DESCRIPTION


def main():
    run_game(find_even_number, DESCRIPTION)


if __name__ == '__main__':
    main()
