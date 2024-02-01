from random import randint
#target = "Answer 'yes' if the number is even, otherwise answer 'no'."


def game_even():
    target = "Answer 'yes' if the number is even, otherwise answer 'no'."
    print(target)
    number = randint(1, 101)
    print('Question: ' + str(number))
    answer = input('Your answer: '.lower())
    if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
        return 'Correct!'
        #return True
    else:
            if answer == 'yes':
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again")
            return False

#game()
