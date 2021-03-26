from collections import defaultdict

def dict_group_tuple_pairs(values):
    result = defaultdict(list)
    for x in values:
        result[x[0]].append(x[1])
    print(dict(result))

values = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dict_group_tuple_pairs(values)
