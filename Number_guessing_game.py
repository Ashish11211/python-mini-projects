import random

secret_number = random.randint(1, 10)

while True:

    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("Correct Guess!")
        break

    elif guess > secret_number:
        print("Too High")

    else:
        print("Too Low")
