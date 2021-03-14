def bitwise_addition(a, b):
    data = 0
    while (b != 0):
        data = a & b
        a = a ^ b
        b = data << 1
    return a

values = [(2,10), (-20,10), (-10,-20)]

for n in values:
    result = bitwise_addition(*n)
    print(result)
