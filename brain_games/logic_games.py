from brain_games.cli import welcome_name
from brain_games.variables import message_repeat, congratulations
# from brain_games.games.gcd import game_gcd, exercise_gcd
# from brain_games.games.progression import game_progression, exercise_progress
# from brain_games.games.prime import game_prime, exercise_prime
# from brain_games.games.calc import game_calc, exercise_calc
# from brain_games.games.even import game_even, exercise_even


def logic(game_name, exercise):
    name = welcome_name()
    round_game = 3
    counter = 0
    print(exercise)
    while counter != round_game:
        result_func = game_name()
        if result_func is True:
            print("Correct!")
            counter += 1
        else:
            counter = 0
            print(f"{message_repeat} {name}")
    return print(f"{congratulations}, {name}")


# logic(game_calc)
# logic(game_even)
# logic(game_gcd)
# logic(game_progression, exercise_progression)
# logic(game_prime)
