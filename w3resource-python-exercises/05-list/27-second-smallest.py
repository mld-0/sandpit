
def second_smallest(values):
    values_set = set(values)
    if len(values_set) < 2:
        print(None)
        return
    values_set_sorted = sorted(values_set)
    result = values_set_sorted[1]
    print(result)

second_smallest([1, 2, -8, -2, 0, -2])
second_smallest([1, 1, 0, 0, 2, -2, -2])
second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2])
second_smallest([2,2])
second_smallest([2])
