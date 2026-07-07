import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

            if difficulty == "easy":
                return EASY_LEVEL_TURNS

            elif difficulty == "hard":
                return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the guessing game!")
    print("I am thinking of a number between 1 and 100")
    secret_number = random.randint(1, 100)
    attempt = set_difficulty()


    while attempt > 0:
        
                print(f"You have {attempt} attempts remaining to guess the number")
                guess = int(input("Make a guess: "))

                if guess > secret_number:
                        print(f"Too high.\n"
                                f"Guess again.\n")
                        attempt -= 1


                elif guess < secret_number:
                            print(f"Too low.\n"
                                  f"Guess again.\n")
                            attempt -= 1

                else:
                        print(f"You got it!The number was {secret_number}.")
                        print("\n" * 100)
                        break


                if attempt == 0:
                    print(f"You've run out of guesses!The number was {secret_number}.")
                    
game()