
def iter_consecutive_items(values):
    result = []
    for i in range(len(values)-1):
        x = values[i]
        y = values[i+1]
        result.append((x, y))
    print(result)

values = [1, 1, 2, 3, 3, 4, 4, 5]
iter_consecutive_items(values)
