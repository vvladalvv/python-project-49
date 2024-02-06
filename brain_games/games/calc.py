from random import choice, randint
from brain_games.variables import incorrect_answer, error_enter_number
exercise_calc = 'What is the result of the expression?'


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
        print(error_enter_number)
        return False
    if answer == num_2 + num_1 and choice_operator == '+':
        return True
    elif answer == num_2 * num_1 and choice_operator == '*':
        return True
    elif answer == num_2 - num_1 and choice_operator == '-':
        return True
    else:
        print(f'{answer} {incorrect_answer} {result}')
        return False

# game_calc()
