from random import randint
from brain_games.constants import INCORRECT_ANSWER
from brain_games.constants import ANSWER_YES, ANSWER_NO
EXERCISE_EVEN = "Answer 'yes' if the number is even, otherwise answer 'no'."


def game_even():
    random_number = randint(1, 101)
    print(f"Question: {random_number}")
    answer = input('Your answer: ').lower()
    if random_number % 2 == 0 and answer == ANSWER_YES:
        return True
    elif random_number % 2 != 0 and answer == ANSWER_NO:
        return True
    else:
        if answer == ANSWER_YES:
            print(f"'{answer}' {INCORRECT_ANSWER} '{ANSWER_NO}'")
        else:
            print(f"'{answer}' {INCORRECT_ANSWER} '{ANSWER_YES}'")
        return False


# game_even()
