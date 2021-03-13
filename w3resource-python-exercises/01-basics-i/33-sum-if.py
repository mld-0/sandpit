def sum_if(a, b, c):
    if (a == b) or (b == c) or (a == c):
        return 0
    return a + b + c

print(sum_if(2, 1, 2))
print(sum_if(3, 2, 2))
print(sum_if(2, 2, 2))
print(sum_if(1, 2, 3))
