from random import randint
from prompt import string
DESCRIPTION_EVEN = "Answer 'yes' if the number is even, otherwise answer 'no'."
ANSWER_YES = 'YES'.lower()
ANSWER_NO = 'NO'.lower()
LOWER_LIMIT = 1
UPPER_LIMIT = 101


def find_even_number():
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    answer_user = string(f"Question: {random_number}\nYour answer: ").lower()
    if random_number % 2 == 0:
        correct_answer = ANSWER_YES
    else:
        correct_answer = ANSWER_NO
    return correct_answer, answer_user

# game_even()
