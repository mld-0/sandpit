x = 1

try:
    x
except NameError:
    print("x, Not Defined")
else:
    print("x, Defined")

try:
    y
except NameError:
    print("y, Not Defined")
else:
    print("y, Defined")


