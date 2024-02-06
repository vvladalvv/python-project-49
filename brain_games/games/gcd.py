from random import randint
import math
from brain_games.constants import INCORRECT_ANSWER, ERROR_ENTER_NUMBER
EXERCISE_GCD = 'Find the greatest common divisor of given numbers.'


def game_gcd():
    num_1 = randint(1, 20)
    num_2 = randint(1, 60)
    gcd = math.gcd(num_1, num_2)
    # print(gcd)
    try:
        answer = int(input(f"Question: {num_1} {num_2}\nYour answer: "))
    except ValueError:
        print(ERROR_ENTER_NUMBER)
        return False
    if answer == gcd:
        return True
    else:
        print(f"'{answer}' {INCORRECT_ANSWER} '{gcd}'")
        return False


# game_gcd()
