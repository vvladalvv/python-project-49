#!/usr/bin/env python3
from brain_games.logic_games import run_game
from brain_games.games.calc import get_question_and_answer, DESCRIPTION


def main():
    run_game(get_question_and_answer, DESCRIPTION)


if __name__ == '__main__':
    main()
