from random import choice, randint

def game_calc():
    operator = ['+', '-', '*']
    choice_operator = choice(operator)
    num_1 = randint(1, 10)
    num_2 = randint(10, 15)
    question = f"Question: {num_2} {choice_operator} {num_1}"
    result = eval(f"{num_2} {choice_operator} {num_1}")
    print('What is the result of the expression?')
    print(question)
    try:
         answer = int(input("Your answer: "))
    except ValueError:
        print('Please, enter a number')
        return False
    if answer == str(answer):
        print('Please, enter a number')
        return False
    elif answer == num_2 + num_1 and choice_operator == '+':
          return 'Correct!'
    elif answer == num_2 * num_1 and choice_operator == '*':
          return 'Correct!'
    elif answer == num_2 - num_1 and choice_operator == '-':
          return 'Correct!'
    else:
        print(f'{answer} Wrong answer! Correct answer is {result}')
        return False

#game_calc()