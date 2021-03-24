
def nested_is_subset(a, b):
    result = False
    for na in a:
        for nb in b:
            if na == nb:
                result = True
    #   or
    result = any(map(a.__contains__, b))
    print(result)

a = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
b = [[1, 3], [13, 15, 17]]
nested_is_subset(a, b)

a = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
b = [[[3, 4], [5, 6]]]
nested_is_subset(a, b)

a = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
b = [[[3, 4], [5, 6]]]
nested_is_subset(a, b)
