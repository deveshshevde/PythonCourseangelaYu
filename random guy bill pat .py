import random

string = input()
string = string.split(" ")

print(string)
x = len(string)
c = random.randint(0, x)

print(string[c])
