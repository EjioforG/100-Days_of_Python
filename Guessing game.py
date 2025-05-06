import random
import os
randguess = random.randint(1, 100)
print("Welcome to the number Guessing game! ")
print("I'm thinking of a number")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while difficulty not in ['easy', 'hard']:
    print("Invalid difficulty level. Please enter 'easy' or 'hard'.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

end_game = False
if difficulty == 'easy':
    total_attempts = 10
elif difficulty == 'hard':
    total_attempts = 5


def game():
    global end_game
    while end_game == False:
        global total_attempts
        print(f"You have {total_attempts} remaining to guess the number ")
        if total_attempts > 0:
            try:
                guess = int(input("Make guess: "))
            except ValueError:
                print("Please enter a valid number")
                continue 
            
            total_attempts-=1

            if guess > randguess:
                print("Too High")
                print("Try again")
            elif guess < randguess:
                print("Too Low")
                print("Try again")
            else:
                end_game = True
                print("Game over u win")

        else:
            end_game = True
            print(f"Out of guesses! You lose. The number was {randguess}.")
           


game()

    
            

        

    



