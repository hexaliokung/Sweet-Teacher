import random

LOWEST_NUM = 1
HIGHEST_NUM = 100
ANSWER = random.randint(LOWEST_NUM, HIGHEST_NUM)
GUESSES = 0
IS_RUNNING = True

print("Python Number Guessing Game")
print(f"Select a number between {LOWEST_NUM} and {HIGHEST_NUM}")

while IS_RUNNING:
    GUESS = input("Enter your guess: ")

    if GUESS.isdigit():
        GUESS = int(GUESS)
        GUESSES += 1
        if GUESS < LOWEST_NUM or GUESS > HIGHEST_NUM:
            print("That number is out of range")
            print(f"Please select a number between {LOWEST_NUM} and {HIGHEST_NUM}")
        elif GUESS < ANSWER:
            print(f"{GUESS} Too low! Try again!")
        elif GUESS > ANSWER:
            print(f"{GUESS} Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {ANSWER}")
            print(f"Number of guesses: {GUESSES}")
            IS_RUNNING = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {LOWEST_NUM} and {HIGHEST_NUM}")