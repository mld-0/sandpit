
def consecutive_num_diff(values):
    result = [values[i+1] - values[i] for i in range(0, len(values)-1)]
    #   or
    result = [b-a for a, b in zip(values[:-1], values[1:])]
    print(result)

values = [1, 1, 3, 4, 4, 5, 6, 7]
consecutive_num_diff(values)

values = [4, 5, 8, 9, 6, 10]
consecutive_num_diff(values)

