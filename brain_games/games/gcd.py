from random import randint
import math
def game_gcd():
    num_1 = randint(1, 20)
    num_2 = randint(1, 60)
    gcd = math.gcd(num_1, num_2)
    print(gcd)
    try:
        answer = int(input(f"Question: {num_1} {num_2}\nYour answer: "))
    except ValueError:
        print('Please, enter a number')
        return False
    if answer == gcd:
        return 'Correct!'
    else:
        print(f"{answer} Wrong answer! Correct answer is {gcd}")
        return False

#game_gcd()
