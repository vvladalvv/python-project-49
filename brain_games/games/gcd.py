from random import randint
from math import gcd
from prompt import integer
DESCRIPTION_GCD = 'Find the greatest common divisor of given numbers.'
LOWER_LIMIT = 1
UPPER_LIMIT = 60


def find_gcd():
    random_num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    random_num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = gcd(random_num_1, random_num_2)
    answer_user = integer(f"Question: {random_num_1} {random_num_2}\nYour answer: ")
    return correct_answer, answer_user

# game_gcd()
