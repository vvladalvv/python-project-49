from random import choice, randint
from brain_games.constants import INCORRECT_ANSWER, ERROR_ENTER_NUMBER
EXERCISE_CALC = 'What is the result of the expression?'


def game_calc():
    operator = ['+', '-', '*']
    choice_operator = choice(operator)
    random_num_1 = randint(1, 10)
    random_num_2 = randint(10, 15)
    question = f"Question: {random_num_2} {choice_operator} {random_num_1}"
    result = eval(f"{random_num_2} {choice_operator} {random_num_1}")
    print(question)
    try:
        answer = int(input("Your answer: "))
    except ValueError:
        print(ERROR_ENTER_NUMBER)
        return False
    if answer == result:
        return True
    else:
        print(f'{answer} {INCORRECT_ANSWER} {result}')
        return False

# game_calc()
