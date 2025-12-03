import random
import time

def number_guess(a, b):
    if a < 0:
        return "Enter a positive number"
    elif a == b:
        return " Correct guess!"
    elif a < b / 2:
        return "Too much smaller"
    elif a < b:
        return "Smaller"
    elif a > b * 1.3:
        return "Much greater"
    elif a > b:
        return "Greater"
    else:
        return "Incorrect"

def main():
    b = random.randint(1, 100)
    attempts = 5

    print("Guess the number between 1 and 50 (You have 5 attempts, 15 sec each)")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        start_time = time.time()

        a = int(input("Enter your guess: "))
        end_time = time.time()
        elapsed = end_time - start_time
        if elapsed > 15:
            print("Time over! You took", int(elapsed), "seconds.")
            attempts -= 1
            continue

        result = number_guess(a, b)
        print(result)

        if a == b:
            print("You guessed it correctly in", 6 - attempts, "attempt(s)!")
            break

        attempts -= 1

    if attempts == 0:
        print("\n Out of attempts!")
        print("The correct number was:", b)

main()
