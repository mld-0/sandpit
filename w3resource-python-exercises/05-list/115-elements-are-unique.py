
def elements_are_unique(values):
    result = len(values) == len(set(values))
    print(result)

values = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
elements_are_unique(values)

values = [2, 4, 6, 8, 10, 12, 14]
elements_are_unique(values)
