from random import choice, randint
DESCRIPTION = "What number is missing in the progression?"
LOWER_LIMIT = 5
UPPER_LIMIT = 15


def give_progression(num_1, step, long):
    progression = []
    for _ in range(long):
        num_1 += step
        progression.append(num_1)
    return progression


def find_progression():
    random_num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    step = randint(LOWER_LIMIT, UPPER_LIMIT)
    long_progression = randint(LOWER_LIMIT, UPPER_LIMIT)
    progression = give_progression(random_num_1, step, long_progression)
    random_num_in_progression = choice(progression)
    index = progression.index(random_num_in_progression)
    progression[index] = '..'
    progression = " ".join(map(str, progression))
    return str(random_num_in_progression), progression

# game_progression()
