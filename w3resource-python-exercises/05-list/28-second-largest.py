
def second_largest(values):
    values_set = set(values)
    if len(values_set) < 2:
        print(None)
        return
    values_set_sorted = sorted(values_set, reverse=True)
    result = values_set_sorted[1]
    print(result)

second_largest([1,2,3,4,4])
second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2])
second_largest([2,2])
second_largest([1])
