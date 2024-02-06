from random import randint
from brain_games.variables import incorrect_answer
from brain_games.variables import answer_yes, answer_no
exercise_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def checkPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def game_prime():
    num_1 = randint(1, 102)
    answer = input(f'Question: {num_1}\nYour answer: ').lower()
    res = checkPrime(num_1)
    if res and answer == answer_yes:
        return True
    elif not res and answer == answer_no:
        return True
    else:
        if answer == answer_yes:
            print(f"'{answer}' {incorrect_answer} '{answer_no}'")
            return False
        else:
            print(f"'{answer}' {incorrect_answer} '{answer_yes}'")
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
