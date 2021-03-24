
def sum_between_range(values, a, b):
    result = sum([values[i] for i in range(a, b+1)])
    print(result)

values = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
sum_between_range(values, 8, 10)
