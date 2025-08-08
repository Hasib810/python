letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '&']

print("welcome to password maker")

r_letters = int(input("how many letters you want in your password?\n" ))
r_numbers = int(input("how many numbers you want in your password?\n" ))
r_symbols = int(input("how many symbols you want in your password?\n" ))
import random
#easylevel

#password = ""
# for char in range(0, r_letters):
#    password += random.choice(letters)
# for char in range(0, r_numbers):
#    password += random.choice(numbers)
# for char in range(0, r_symbols):
#    password += random.choice(symbols)
# print(password)

#hard level 
password_list = []
for char in range(0, r_letters):
   password_list.append(random.choice(letters))
for char in range(0, r_numbers):
   password_list.append(random.choice(numbers))
for char in range(0, r_symbols):
   password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ""
for char in password_list:
   password += char
print(f"password is {password}")
   


