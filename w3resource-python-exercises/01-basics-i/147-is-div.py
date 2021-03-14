def is_divisible(a, b):
    print(f"a=({a}), b=({b})")
    if (a % b == 0):
        print(True)
    else:
        print(False)

values = [(20, 5), (7, 5)]

for val in values:
    is_divisible(*val)

