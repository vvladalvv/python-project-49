#!/usr/bin/env python3
import random
from prompt import string
#from brain_games.scripts.brain_games import main
#from brain_games.cli import welcome_user
#main()
#welcome_user()


def welcome():
    print("Welcome to the Brain Games!")

welcome()
name = string("May I have your name? ")

def welcome_user():
    return print("Hello, " + name + "!")

welcome_user()

def main():
    #import random
    #number = random.randint(1, 100)
    #print(number)
    #answer = input('Question: ')
    #ans = 'YES' or 'NO'
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    counter = 0
    while counter != 3:
        number = random.randint(1, 100)
        print(number)
        answer = input('Question: '.lower())
        if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
            print('Correct!')
            counter += 1
            #break
        else:
            if answer == 'yes':
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,{name}")
                counter = 0
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,{name}")
                counter = 0
            #break
    print(f"Congratulations, {name}")

if __name__ == '__main__':
    main()
