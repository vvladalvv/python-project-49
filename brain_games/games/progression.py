from random import choice, randint
from brain_games.variables import incorrect_answer, error_enter_number
exercise_progress = "What number is missing in the progression?"


def game_progression():
    num_1 = randint(1, 10)
    step = randint(1, 8)
    long_progression = randint(5, 15)
    progression = []
    for i in range(long_progression):
        num_1 += step
        progression.append(num_1)
    random_num = choice(progression)
    index = progression.index(random_num)
    progression[index] = '...'
    try:
        answer = int(input(f"Question: {progression}\nYour answer: "))
    except ValueError:
        print(error_enter_number)
        return False
    if answer == random_num:
        return True
    else:
        print(f"'{answer}' {incorrect_answer} '{random_num}'")
        return False


# game_progression()
