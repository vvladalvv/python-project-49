from random import randint
from math import gcd
DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LOWER_LIMIT = 1
UPPER_LIMIT = 60


def find_gcd():
    num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = gcd(num_1, num_2)
    question = f"{num_1} {num_2}"
    return str(correct_answer), question

# game_gcd()
