def sum_if(a, b, c):
    if (a == b) and (b == c):
        print(3 * (a + b + c))
    else:
        print(a + b + c)

vals = [[1, 2, 3], [3, 3, 3]]

for n in vals:
    sum_if(*n)
