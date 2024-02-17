from random import randint
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
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
    question = f"{random_number}"
    return correct_result, question

# game_prime()
