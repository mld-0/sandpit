
def flatten_nested_list(values):
    result = []
    for x in values:
        if isinstance(x, list):
            for y in x:
                result.append(y)
        else:
            result.append(x)
    print(result)

values = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flatten_nested_list(values)

