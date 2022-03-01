#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

random_placement = random.randint(1,101)


for char in range(1, nr_letters +1):
    randomizer_letter_ez = random.randint(1, len(letters) -1)
    r_letter = letters[randomizer_letter_ez]
    password_list += r_letter

for num in range(1, nr_numbers +1):
    randomizer_numbers_ez = random.randint(1, len(numbers) -1)
    r_number = numbers[randomizer_numbers_ez]
    password_list += r_number

for sym in range(1, nr_symbols +1):
    randomizer_symbols_ez = random.randint(1, len(symbols) -1)
    r_symbol = symbols[randomizer_symbols_ez]
    password_list += r_symbol

random.shuffle(password_list)
password_final = ''.join(password_list)

print(password_final)
  


