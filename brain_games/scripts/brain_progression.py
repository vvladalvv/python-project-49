#!/usr/bin/env python3
from brain_games.logic_games import run_game
from brain_games.games.progression import find_progression, DESCRIPTION


def main():
    run_game(find_progression, DESCRIPTION)


if __name__ == '__main__':
    main()
