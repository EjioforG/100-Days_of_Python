import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "*", "$", "(", ")", "#", "&", "+", "-"]

print("Welcome to Godswill python password generator ")
nr_letters = int(input("How many letters do you like: "))
nr_symbols = int(input("How many symbols do you like: "))
nr_numbers = int(input("How many numbers do you like: "))

# Easy level

password = ""

for n in range(0, nr_letters):
    rand = random.choice(letters)
    password += rand
for n in range(0, nr_symbols):
    rand2 = random.choice(symbols)
    password += rand2
for n in range(0, nr_numbers):
    rand3 = random.choice(numbers)
    password += rand3

# print(password)

# Hard level 
password2 = []

for n in range(0, nr_letters):
    rand = random.choice(letters)
    password2 +=rand
for n in range(0, nr_symbols):
    rand2 = random.choice(symbols)
    password2 +=rand2
for n in range(0, nr_numbers):
    rand3 = random.choice(numbers)
    password2 +=rand3

    

# print(password2)

random.shuffle(password2)
# print(password2)

non_list_pass = ""
for n in password2:
    non_list_pass += n
print(non_list_pass)




