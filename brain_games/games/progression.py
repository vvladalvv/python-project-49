from random import choice, randint


def game_progression():
    num_1 = randint(1, 10)
    step = randint(1, 8)
    long_progression = randint(5, 15)
    progression = []
    print("What number is missing in the progression?")
    for i in range(long_progression):
        num_1 += step
        progression.append(num_1)
    
    random_num = choice(progression)
    index = progression.index(random_num)
    progression[index] = '...'
    try:
        answer = int(input(f"Question: {progression}\nYour answer: "))
    except ValueError:
        print('Please, enter a number')
        return False
    if answer == random_num:
        return 'Correct!'
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {random_num}")
        return False

#game_progression()