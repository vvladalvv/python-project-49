#!/usr/bin/env python3
from brain_games.logic_games import run_game
from brain_games.games.calc import get_calc, DESCRIPTION


def main():
    run_game(get_calc, DESCRIPTION)


if __name__ == '__main__':
    main()
