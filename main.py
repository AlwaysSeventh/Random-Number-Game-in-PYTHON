#random number game!
from random import randint

user_tries = 5
# VARIABLES
range_1 = randint(1,10)
range_2 = randint(1,1000)
game_answer = randint(range_1, range_2)

str_range_1 = str(range_1)
str_range_2 = str(range_2)
str_game_answer = str(game_answer)

hint_1 = str(game_answer - 5)
hint_2 = str(game_answer + 5)

while True:
    if (user_tries > 0):
        user_guess = int(input(f'"Guess a number between {str_range_1} and {str_range_2}"'))
        if (user_guess > range_1):
            if (user_guess != game_answer):
                user_tries = user_tries - 1
                print(f'"Try again! You have {user_tries} tries!"')
                if (user_tries < 3):
                    print("Take a hint! You have less than 3 tries!!")
                    print(f'"The number is between {hint_1} and {hint_2}"')
            else:
                print(f'"You win! Nice GUESS! The number was {game_answer}"')
                break
        else:
            print(f'"Please guess a number higher than {range_1}"')
    else:
        print(f'"You lost! The number was {game_answer}"')
        break
