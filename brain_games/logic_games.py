from brain_games.games.even import game_even
from brain_games.games.calc import game_calc
from brain_games.cli import welcome_name
from brain_games.games.gcd import game_gcd
from brain_games.games.progression import game_progression



def logic(game_name):
    name = welcome_name()
    #print(target)
    round_game = 3
    counter = 0
    while counter != round_game:
        output_func = game_name()
        if output_func:
            print(output_func)
            counter += 1
            #print(str(counter) + ' - round пройден')
        else: 
            #counter += 1
            #print(str(counter) + ' - round непройден')
            counter = 0 
    return print('Congratulations, ' + name)

#logic(game_calc)
#logic(game_even)  
#logic(game_gcd)
#logic(game_progression)