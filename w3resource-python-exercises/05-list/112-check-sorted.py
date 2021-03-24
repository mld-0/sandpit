
def check_sorted(values):
    result = values == sorted(values)
    #   or
    result = all([values[i] < values[i+1] for i in range(0, len(values)-1)])
    print(result)

values = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
check_sorted(values)

values = [1, 2, 4, 6, 11, 10, 12, 14, 16, 17]
check_sorted(values)
