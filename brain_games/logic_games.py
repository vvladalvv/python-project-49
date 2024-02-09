from brain_games.cli import welcome_name
from brain_games.constants import MESSAGE_REPEAT, CONGRATULATIONS
# from brain_games.games.gcd import game_gcd, EXERCISE_GCD
# from brain_games.games.progression import game_progression, EXERCISE_PROGRESS
# from brain_games.games.prime import game_prime, EXERCISE_PRIME
# from brain_games.games.calc import game_calc, EXERCISE_CALC
from brain_games.games.even import game_even, EXERCISE_EVEN


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
            print(f"{MESSAGE_REPEAT} {name} !")
    return print(f"{CONGRATULATIONS}, {name} !")


# logic(game_calc, EXERCISE_CALC)
logic(game_even, EXERCISE_EVEN)
# logic(game_gcd, EXERCISE_GCD)
# logic(game_progression, EXERCISE_PROGRESS)
# logic(game_prime, EXERCISE_PRIME)
