def sum_if(a, b):
    result = a + b
    if (result >= 15) and (result <= 20):
        return 20
    else:
        return result

print(sum_if(10, 6))
print(sum_if(10, 2))
print(sum_if(10, 12))
