from random import choice, randint
from brain_games.constants import INCORRECT_ANSWER, ERROR_ENTER_NUMBER
EXERCISE_CALC = 'What is the result of the expression?'


def game_calc():
    operator = ['+', '-', '*']
    choice_operator = choice(operator)
    num_1 = randint(1, 10)
    num_2 = randint(10, 15)
    question = f"Question: {num_2} {choice_operator} {num_1}"
    result = eval(f"{num_2} {choice_operator} {num_1}")
    print(question)
    try:
        answer = int(input("Your answer: "))
    except ValueError:
        print(ERROR_ENTER_NUMBER)
        return False
    if answer == num_2 + num_1 and choice_operator == '+':
        return True
    elif answer == num_2 * num_1 and choice_operator == '*':
        return True
    elif answer == num_2 - num_1 and choice_operator == '-':
        return True
    else:
        print(f'{answer} {INCORRECT_ANSWER} {result}')
        return False

# game_calc()
