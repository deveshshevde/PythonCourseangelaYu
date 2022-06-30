import random

passlist = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

let = int(input("How many letters you need in password"))
num = int(input("How many numbers you need in password"))
sym = int(input("How many symbols you need in password"))
for x in range(0, let):
    let_i = random.randint(0, len(letters) - 1)
    passlist.append(letters[let_i])

for y in range(0, num):
    num_i = random.randint(0, len(numbers) - 1)
    passlist.append(numbers[num_i])

for z in range(0, sym):
    sym_i = random.randint(0, len(symbols) - 1)
    passlist.append(symbols[sym_i])

random.shuffle(passlist)

for i in range(0, len(passlist)):
    password += passlist[i]

print(password)
