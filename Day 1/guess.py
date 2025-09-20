import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Try to guess it!")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
