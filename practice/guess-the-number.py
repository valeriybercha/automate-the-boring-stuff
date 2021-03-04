# Guess the number game
# Developer: Valery B.
# Language: Python 3.8.5

import random

# Random number from 1 to 20
def randomizer():
    return random.randint(1, 20)

# Game logic
def gues_the_number():
    
    # Welcome message
    print("I'm thinking of a number between 1 and 20")

    # Random number variable
    number_to_guess = randomizer()

    # Counting and guess variables
    count = 1
    guess = 0
    
    # Looping six times to guess the number
    for i in range(6):
        print("Take a guess.")
        guess = int(input())

        # Guess result logic
        if guess > number_to_guess:
            print("Your guess is too high")
            count += 1
        elif guess < number_to_guess:
            print("Your guess is too low")
            count += 1
        else:
            break
    
    # Printing the final result
    if number_to_guess == guess:
        print(f"Good job! You guessed my number in {count} guesses!")
    else:
        print(f"Nope. The number I was thinking was {number_to_guess}")


gues_the_number()