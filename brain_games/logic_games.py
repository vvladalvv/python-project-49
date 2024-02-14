from brain_games.cli import welcome_user
# from brain_games.games.gcd import find_gcd, DESCRIPTION
# from brain_games.games.progression import find_progression, DESCRIPTION
# from brain_games.games.prime import find_prime_number, DESCRIPTION
# from brain_games.games.calc import get_question_and_answer, DESCRIPTION
# from brain_games.games.even import find_even_number, DESCRIPTION


INCORRECT_ANSWER = 'is wrong answer ;(. Correct answer was'
MESSAGE_REPEAT = "Let's try again"
CONGRATULATIONS = "Congratulations"


def check_answer(correct_answer, user_answer):
    if user_answer == correct_answer:
        return user_answer
    else:
        return correct_answer


def run_game(game_name, description):
    name = welcome_user()
    round_game = 3
    counter_correct = 1
    correct_round = 0
    print(description)
    while correct_round != round_game:
        result_func = game_name()
        correct_answer, user_answer = result_func
        check_answer(correct_answer, user_answer)
        if user_answer == correct_answer:
            print("Correct!")
            correct_round += counter_correct
        else:
            correct_round = 0
            print(f"'{user_answer}' {INCORRECT_ANSWER}, '{correct_answer}'.")
            print(f"{MESSAGE_REPEAT}, {name}!")
            return
    return print(f"{CONGRATULATIONS}, {name}!")


# run_game(get_question_and_answer, DESCRIPTION)
# run_game(find_even_number, DESCRIPTION)
# run_game(find_gcd, DESCRIPTION)
# run_game(find_progression, DESCRIPTION)
# run_game(find_prime_number, DESCRIPTION)
