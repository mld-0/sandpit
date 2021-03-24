from collections import Counter

def unique_sublists_count(values):
    values_tuples = [tuple(x) for x in values]
    result = Counter(values_tuples)
    print(result)

values = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
unique_sublists_count(values)

values = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
unique_sublists_count(values)

