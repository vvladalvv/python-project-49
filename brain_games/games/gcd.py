from random import randint
import math
from brain_games.variables import incorrect_answer, error_enter_number
exercise_gcd = 'Find the greatest common divisor of given numbers.'


def game_gcd():
    num_1 = randint(1, 20)
    num_2 = randint(1, 60)
    gcd = math.gcd(num_1, num_2)
    # print(gcd)
    try:
        answer = int(input(f"Question: {num_1} {num_2}\nYour answer: "))
    except ValueError:
        print(error_enter_number)
        return False
    if answer == gcd:
        return True
    else:
        print(f"'{answer}' {incorrect_answer} '{gcd}'")
        return False


# game_gcd()
