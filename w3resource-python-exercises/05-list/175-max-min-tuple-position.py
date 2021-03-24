
def max_min_tuple_position(values):
    values_inverted_max = [max(x) for x in zip(*values)]
    values_inverted_min = [min(x) for x in zip(*values)]
    print(values_inverted_max)
    print(values_inverted_min)

values = [(2, 3), (2, 4), (0, 6), (7, 1)]
max_min_tuple_position(values)

