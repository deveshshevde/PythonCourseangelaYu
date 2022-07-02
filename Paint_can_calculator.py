import math

h = int(input("Enter the height"))
w = int(input("Enter the width"))
coverage = int(input("Enter the coverage"))


def print_no_of_can(h, w, coverage):
    x = (h * w) / coverage
    print(math.ceil(x))


print_no_of_can(h, w, coverage)
