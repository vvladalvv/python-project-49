from random import randint
from brain_games.variables import incorrect_answer
from brain_games.variables import answer_yes, answer_no
exercise_even = "Answer 'yes' if the number is even, otherwise answer 'no'."


def game_even():
    number = randint(1, 101)
    print('Question: ' + str(number))
    answer = input('Your answer: ').lower()
    if number % 2 == 0 and answer == answer_yes:
        return True
    if number % 2 != 0 and answer == answer_no:
        return True
    else:
        if answer == answer_yes:
            print(f"'{answer}' {incorrect_answer} '{answer_no}'")
        else:
            print(f"'{answer}' {incorrect_answer} '{answer_yes}'")
        return False


# game_even()
