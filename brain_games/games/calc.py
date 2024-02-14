from random import choice, randint
from prompt import integer
DESCRIPTION = 'What is the result of the expression?'
OPERATOR = ('+', '-', '*')
LOWER_LIMIT = 1
UPPER_LIMIT = 15


def give_an_example():
    choice_operator = choice(OPERATOR)
    random_num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    random_num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f"Question: {random_num_2} {choice_operator} {random_num_1}"
    print(question)
    if choice_operator == '-':
        result = random_num_2 - random_num_1
    if choice_operator == '+':
        result = random_num_2 + random_num_1
    if choice_operator == '*':
        result = random_num_2 * random_num_1
    return result


def get_question_and_answer():
    correct_result = give_an_example()
    answer_user = integer("Your answer: ")
    return correct_result, answer_user

# game_calc()
