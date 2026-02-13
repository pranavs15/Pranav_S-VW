# Question 3:
# Number Guessing Game
# The computer selects a random number (1–100).
# Player has 7 attempts to guess correctly.

import random

secret_number = random.randint(1, 100)
attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")
print("You have 7 attempts.\n")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess > secret_number:
        print("Too high! Try a smaller number.\n")
    elif guess < secret_number:
        print("Too low! Try a larger number.\n")
    else:
        print("🎉 Congratulations! You guessed the number correctly!")
        break
else:
    print(f"\n❌ You lost! The correct number was {secret_number}.")
