from brain_games.cli import welcome_user
from prompt import string
# from brain_games.games.gcd import find_gcd, DESCRIPTION
# from brain_games.games.progression import find_progression, DESCRIPTION
# from brain_games.games.prime import find_prime_number, DESCRIPTION
# from brain_games.games.calc import get_calc, DESCRIPTION
# from brain_games.games.even import find_even_number, DESCRIPTION


INCORRECT_ANSWER = 'is wrong answer ;(. Correct answer was'
MESSAGE_REPEAT = "Let's try again"
CONGRATULATIONS = "Congratulations"
ROUND_GAME = 3


def run_game(get_question_and_answer, description):
    name = welcome_user()
    print(description)
    for _ in range(ROUND_GAME):
        correct_answer, question = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' {INCORRECT_ANSWER}, '{correct_answer}'.")
            print(f"{MESSAGE_REPEAT}, {name}!")
            return
        print("Correct!")
    return print(f"{CONGRATULATIONS}, {name}!")


# run_game(get_calc, DESCRIPTION)
# run_game(find_even_number, DESCRIPTION)
# run_game(find_gcd, DESCRIPTION)
# run_game(find_progression, DESCRIPTION)
# run_game(find_prime_number, DESCRIPTION)
