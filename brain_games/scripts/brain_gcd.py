#!/usr/bin/env python3
from brain_games.logic_games import logic
from brain_games.games.gcd import game_gcd, EXERCISE_GCD


def main():
    logic(game_gcd, EXERCISE_GCD)


if __name__ == '__main__':
    main()
