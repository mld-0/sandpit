
def max_min_hetrogeneous_list(values):
    values_numeric = [x for x in values if isinstance(x, int) or isinstance(x, float)]
    _max = max(values_numeric)
    _min = min(values_numeric)
    print(_max, _min)

values = ['Python', 3, 2, 4, 5, 'version']
max_min_hetrogeneous_list(values)
