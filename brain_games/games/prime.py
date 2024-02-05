from random import randint


def game_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num_1 = randint(1, 102)
    answer = input(f'Question: {num_1}\nYour answer: ').lower()
    if num_1 == 2 or num_1 == 3 or num_1 == 5 or num_1 == 7:
        if answer == 'yes':
          return 'Correct!'
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again")
            return False
    elif num_1 % 2 == 0 or num_1 % 3 == 0 or num_1 % 5 == 0 or num_1 % 7 == 0 or num_1 % 9 == 0:
        if answer == 'no':
            return 'Correct!'
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again")
            return False
    else:
        if answer == 'yes': 
            return 'Correct!'
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again")
            return False

#game_prime()