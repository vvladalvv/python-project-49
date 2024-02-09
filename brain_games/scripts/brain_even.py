#!/usr/bin/env python3
from brain_games.logic_games import logic
from brain_games.games.even import game_even, EXERCISE_EVEN


def main():
    logic(game_even, EXERCISE_EVEN)


if __name__ == '__main__':
    main()
