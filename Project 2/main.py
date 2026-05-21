import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1

            if guess < target_number:
                print("Higher number please.")

            elif guess > target_number:
                print("Lower number please.")

            else:
                print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            

if __name__ == "__main__":
    number_guessing_game()

    