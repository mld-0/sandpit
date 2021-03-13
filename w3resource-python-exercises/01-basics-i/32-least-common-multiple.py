def least_common_multiple(a, b):
    n = 1
    min_value = min(a, b)
    max_value = max(a, b)
    while (True):
        if ((n*min_value) % max_value == 0):
            return (n*min_value)
        n += 1

print(least_common_multiple(4, 6))
print(least_common_multiple(15, 17))
