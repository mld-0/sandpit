
def index_max_min(values):
    _max = max(values)
    _min = min(values)
    _max_indexes = [i for i in range(len(values)) if values[i] == _max]
    _min_indexes = [i for i in range(len(values)) if values[i] == _min]
    print(_max_indexes)
    print(_min_indexes)

values = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
index_max_min(values)

