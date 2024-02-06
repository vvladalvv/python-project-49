from random import randint
from brain_games.constants import INCORRECT_ANSWER
from brain_games.constants import ANSWER_YES, ANSWER_NO
EXERCISE_EVEN = "Answer 'yes' if the number is even, otherwise answer 'no'."


def game_even():
    number = randint(1, 101)
    print('Question: ' + str(number))
    answer = input('Your answer: ').lower()
    if number % 2 == 0 and answer == ANSWER_YES:
        return True
    if number % 2 != 0 and answer == ANSWER_NO:
        return True
    else:
        if answer == ANSWER_YES:
            print(f"'{answer}' {INCORRECT_ANSWER} '{ANSWER_NO}'")
        else:
            print(f"'{answer}' {INCORRECT_ANSWER} '{ANSWER_YES}'")
        return False


# game_even()
