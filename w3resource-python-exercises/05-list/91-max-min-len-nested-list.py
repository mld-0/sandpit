
def max_min_len_nested_list(values):
    _max = (None, None)
    _min = (None, None)
    for x in values:
        if _max[0] is None or len(x) > _max[0]:
            _max = (len(x), x)
        if _min[0] is None or len(x) < _min[0]:
            _min = (len(x), x)
    print(_max)
    print(_min)

values = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max_min_len_nested_list(values)
print()

values = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
max_min_len_nested_list(values)
print()

values = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
max_min_len_nested_list(values)
        
