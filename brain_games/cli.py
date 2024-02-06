from prompt import string


def welcome_name():
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print("Hello, " + name + "!")
    return name


def welcome_user():
    name = string("May I have your name? ")
    return print("Hello, " + name + "!")
