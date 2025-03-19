
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher(text_, shift_amount, direction_):
    if direction_ == "decode":
            shift_amount *= -1 
    end_text = ""
    for letter in text_:
        if letter in alphabet:   
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
             end_text +=  letter
    print(f"The {direction_}d text is {end_text}")
    

        
from hangman_art2 import logo
print(logo)
end_of_game = False
while not end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()

    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Invalid input! Please enter a shift number: ")
    shift = shift % 26
    cipher(text, shift, direction)
    continue_ = input("Type 'yes' if you want to go again. Otherwise type no.\n").lower()
    if continue_ == 'yes':
        cipher(text, shift, direction)
    elif continue_=='no':
        end_of_game = True
        print("GoodBye")


