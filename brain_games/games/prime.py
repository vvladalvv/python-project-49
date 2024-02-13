from random import randint
from prompt import string
DESCRIPTION_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ANSWER_YES = 'YES'.lower()
ANSWER_NO = 'NO'.lower()
LOWER_LIMIT = 1
UPPER_LIMIT = 102


def check_prime(num):
    if num <= 1:
        return ANSWER_NO
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return ANSWER_NO
    return ANSWER_YES


def find_prime_number():
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_result = check_prime(random_number)
    answer_user = string(f"Question: {random_number}\nYour answer: ").lower()
    return correct_result, answer_user

# game_prime()
