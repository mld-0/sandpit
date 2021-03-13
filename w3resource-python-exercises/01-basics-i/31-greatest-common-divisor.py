def greatest_common_divisor(a, b):
    range_max = max(a, b)
    #for i in range(range_max-1, 0, -1):  # [1, range_max)
    #   or
    for i in reversed(range(int(range_max/2))):  
        if (a % i == 0) and (b % i == 0):
            return i

print(greatest_common_divisor(12, 17))
print(greatest_common_divisor(4, 6))
