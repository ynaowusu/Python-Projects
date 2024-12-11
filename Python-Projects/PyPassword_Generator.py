#password generator 
import random

symbols = ['!','#','$','(',')','*','+']

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

print("Welcome to the PyPassword Generator!")
letter_count = int(input("How many letters would you like in your password? "))
symbol_count = int(input("How many symbols would you like? "))
number_count = int(input("How many numbers would you like? "))

password = " "

for i in range(1 , (letter_count + 1)):
    password += letters[i]


for i in range(1 , (symbol_count + 1)):
    password += symbols[i]

for i in range(1 , (number_count + 1)):
    password += numbers[i]

password_list = list(password)
random.shuffle(password_list)
result = ''.join(password_list)
print(result)

