
def start_end_position(values, n):
    if not n in values:
        print([0, 0])
        return
    values_n_index = [i for i, c in enumerate(values) if c == n]
    print([values_n_index[0], values_n_index[-1]])

start_end_position([5,7,7,8,8,8], 8)
start_end_position([1,3,6,9,13,14], 4)
