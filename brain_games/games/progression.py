from random import choice, randint
from brain_games.constants import INCORRECT_ANSWER, ERROR_ENTER_NUMBER
EXERCISE_PROGRESS = "What number is missing in the progression?"


def game_progression():
    random_num = randint(1, 10)
    step = randint(1, 8)
    long_progression = randint(5, 15)
    progression = []
    for i in range(long_progression):
        random_num += step
        progression.append(random_num)
    random_num_in_progression = choice(progression)
    index = progression.index(random_num_in_progression)
    progression[index] = '...'
    try:
        answer = int(input(f"Question: {progression}\nYour answer: "))
    except ValueError:
        print(ERROR_ENTER_NUMBER)
        return False
    if answer == random_num_in_progression:
        return True
    else:
        print(f"'{answer}' {INCORRECT_ANSWER} '{random_num_in_progression}'")
        return False


# game_progression()
