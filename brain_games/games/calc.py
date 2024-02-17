from random import choice, randint
DESCRIPTION = 'What is the result of the expression?'
OPERATOR = ('+', '-', '*')
LOWER_LIMIT = 1
UPPER_LIMIT = 15


def get_calc():
    choice_operator = choice(OPERATOR)
    random_num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    random_num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f"{random_num_2} {choice_operator} {random_num_1}"
    if choice_operator == '-':
        result = random_num_2 - random_num_1
    if choice_operator == '+':
        result = random_num_2 + random_num_1
    if choice_operator == '*':
        result = random_num_2 * random_num_1
    return str(result), question


# game_calc()
