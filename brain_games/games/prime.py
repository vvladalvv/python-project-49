from random import randint
from brain_games.constants import INCORRECT_ANSWER
from brain_games.constants import ANSWER_YES, ANSWER_NO
EXERCISE_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def game_prime():
    random_number = randint(1, 102)
    result = check_prime(random_number)
    answer = input(f'Question: {random_number}\nYour answer: ').lower()
    if result is True and answer == ANSWER_YES:
        return True
    elif result is not True and answer == ANSWER_NO:
        return True
    else:
        if answer == ANSWER_YES:
            print(f"'{answer}' {INCORRECT_ANSWER} '{ANSWER_NO}'")
        else:
            print(f"'{answer}' {INCORRECT_ANSWER} '{ANSWER_YES}'")
        return False

# if num_1 == 2 or num_1 == 3 or num_1 == 5 or num_1 == 7:
    # if answer == answer_yes:
        # return correct_answer
    # else:
        # print(f"'{answer}' {incorrect_answer} '{answer_yes}'")
        # return False
# elif num_1 % 2 == 0 or num_1 % 3 == 0 or num_1 % 5 == 0:
    # if answer == answer_no:
        # return correct_answer
    # else:
        # print(f"'{answer}' {incorrect_answer} '{answer_no}'")
        # return False
# elif num_1 % 7 == 0 or num_1 % 9 == 0:
    # if answer == answer_no:
        # return correct_answer
    # else:
        # print(f"'{answer}' {incorrect_answer} '{answer_no}'")
        # return False
# else:
    # if answer == answer_yes:
        # return correct_answer
    # else:
        # print(f"'{answer}' {incorrect_answer}' {answer_yes}'")
    # return False

# game_prime()
