
def pair_consecutive(values):
    result = []
    for i in range(len(values)-1):
        x = values[i]
        y = values[i+1]
        result.append([x, y])
    print(result)


values = [1, 2, 3, 4, 5, 6]
pair_consecutive(values)

values = [1, 2, 3, 4, 5]
pair_consecutive(values)

