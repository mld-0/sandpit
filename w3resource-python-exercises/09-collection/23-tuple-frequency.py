from collections import Counter

def tuple_frequency(values):
    values_tuples = []
    for t in values:
        values_tuples.append(tuple(t))
    result_counter = Counter(values_tuples)
    print(result_counter)

values = [['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7']]
tuple_frequency(values)

