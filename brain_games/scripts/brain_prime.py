#!/usr/bin/env python3
from brain_games.logic_games import logic
from brain_games.games.prime import game_prime, EXERCISE_PRIME


def main():
    logic(game_prime, EXERCISE_PRIME)


if __name__ == '__main__':
    main()
