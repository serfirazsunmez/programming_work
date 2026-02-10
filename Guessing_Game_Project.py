# Do a guessing game project
import random

def guess_numbers(number_2):
    random_number = random.randint(5,10)
    while True:
        if number_2 == random_number:
            return "congrats"
        elif number_2 != random_number:
            return "Try again"    
        return random_number

print(guess_numbers(number_2=5))