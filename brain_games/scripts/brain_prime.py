#!/usr/bin/env python3
from brain_games.logic_games import run_game
from brain_games.games.prime import find_prime_number, DESCRIPTION


def main():
    run_game(find_prime_number, DESCRIPTION)


if __name__ == '__main__':
    main()
