import random
word_list = ["ardvark", "baboon",  "camel"]

chosen_word = random.choice(word_list)
print(f"The solution is {chosen_word}")

guess = input("Guess a letter ").lower()

guess_list = []
for _ in chosen_word:
    _ = '_'
    guess_list+=_
#print(guess_list)



position = 0
if guess in chosen_word:
    for n in chosen_word:
        position+=1
        if n == guess:
            #print(position)
            guess_list[position-1] = guess
print(guess_list)
            
#print(guess)
#print(position)

# for guessed_word in chosen_word:
#     if guess == guessed_word:
#         print("Right")
#     else:
#         print("Wrong")

