import random

OPTIONS = ("rock", "paper", "scissors")
RUNNING = True
while RUNNING:
    COMPUTER = random.choice(OPTIONS)
    PLAYER = input("Enter a choice (rock, paper, scissors): ").lower()
    if PLAYER not in OPTIONS:
        print("Invalid choice, please try again.")
        continue
    print(f"Computer chose: {COMPUTER}")
    if PLAYER == COMPUTER:
        print("It's a tie!.")
        continue
    elif(PLAYER == "rock" and COMPUTER == "scissors") or \
        (PLAYER == "scissors" and COMPUTER == "paper") or \
        (PLAYER == "paper" and COMPUTER == "rock"):
        print("You win!")
    else:
        print("You lose!")
    AGAIN =  input("Play again? (y/n)").lower()
    if AGAIN != "y":
        RUNNING = False

print("Thanks for playing!")