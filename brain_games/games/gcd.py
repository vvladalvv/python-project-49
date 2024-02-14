from random import randint
from math import gcd
from prompt import integer
DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LOWER_LIMIT = 1
UPPER_LIMIT = 60


def find_gcd():
    num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = gcd(num_1, num_2)
    answer_user = integer(f"Question: {num_1} {num_2}\nYour answer: ")
    return correct_answer, answer_user

# game_gcd()
