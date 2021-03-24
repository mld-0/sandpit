
def sum_and_divide(values):
    result = []
    for x, y in zip(values[:-1], values[1:]):
        result.append((x+y)/2)
    #   or
    result = [(x+y)/2 for x, y in zip(values[:-1], values[1:])]
    print(result)


values = [1, 2, 3, 4, 5, 6, 7]
sum_and_divide(values)

values = [0, 1, -3, 3, 7, -5, 6, 7, 11]
sum_and_divide(values)

