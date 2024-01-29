from prompt import string


def welcome_user():
    name = string("May I have your name? ")
    return print("Hello, " + name + "!")

