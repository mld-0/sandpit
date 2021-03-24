
def swap_first_last(values):
    result = [values[-1]] + values[1:-1] + [values[0]]
    print(result)

values = [1, 2, 3, 4, 5, 6, 7]
swap_first_last(values)

values = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
swap_first_last(values)
