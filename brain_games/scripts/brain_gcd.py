#!/usr/bin/env python3
from brain_games.logic_games import run_game
from brain_games.games.gcd import find_gcd, DESCRIPTION_GCD


def main():
    run_game(find_gcd, DESCRIPTION_GCD)


if __name__ == '__main__':
    main()
