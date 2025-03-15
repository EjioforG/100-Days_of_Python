import random
from hangman_words import word_list
from hangman_art import logo      
from hangman_art import stages   
print(logo)                       

chosen_word = random.choice(word_list)
print(f"The solution is {chosen_word}")





# guess = input("Guess a letter ").lower()

guess_list = []
for _ in chosen_word:
    _ = '_'
    guess_list+=_
#print(guess_list)
position = 0
lives = 6
still_guessing = True
while still_guessing:
    if "_" in guess_list:
        guess = input("Guess a letter ").lower()
        if guess in guess_list:
            print(f"You have already guessed {guess}")
        #for _ in chosen_word:
        # _ = '_'
            #guess_list+=_

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                guess_list[position] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess} is not in the word, you lose a life")
            print(stages[lives-6])
            if lives == -1:
                print("You lose, out of tries")
                still_guessing = False

        elif still_guessing == False:
            print("You lose")
        # print(lives)
        print(guess_list)

    else:
        still_guessing = False
        print("You win")






