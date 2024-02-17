from random import randint
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
ANSWER_YES = 'YES'.lower()
ANSWER_NO = 'NO'.lower()
LOWER_LIMIT = 1
UPPER_LIMIT = 101


def find_even_number():
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f"{random_number}"
    correct_answer = ANSWER_NO
    if random_number % 2 == 0:
        correct_answer = ANSWER_YES
    return correct_answer, question

# game_even()
