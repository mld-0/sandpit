
def first_two(val, n):
    if (len(val) < 2):
        return val * n
    else:
        start = val[0:2]
        return start * n

print(first_two('abcdef', 2))
print(first_two('p', 3))
