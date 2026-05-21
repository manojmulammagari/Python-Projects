# Number Guessing Game 

A simple, interactive command-line Number Guessing Game written in Python. This is a mini-project to demonstrate loops, conditionals, and user input validation.

## Description

In this game, the computer randomly selects a number between 1 and 100. Your goal is to guess that number in as few attempts as possible. After each guess, the program will give you a hint, telling you whether the hidden number is higher or lower than your guess.

## Features

- **Randomized Gameplay**: A new number is generated every time you play.
- **Input Validation**: The game handles invalid inputs (like letters or symbols) gracefully using `try-except` blocks without crashing.
- **Attempt Tracking**: Keeps count of how many tries it took you to win.

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Clone this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the project directory.
4. Run the script using the following command:

   ```bash
   python main.py
   ```

## Example Output

```text
Welcome to the Number Guessing Game!
Guess the number (between 1 and 100): 50
Higher number please.
Guess the number (between 1 and 100): 75
Lower number please.
Guess the number (between 1 and 100): 62
Congratulations! You guessed the correct number 62 in 3 attempts.
```
