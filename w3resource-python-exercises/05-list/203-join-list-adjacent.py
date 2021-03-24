
def join_list_adjacent(values):
    result = [''.join([values[i], values[i+1]]) for i in range(0, len(values), 2) if i+1 < len(values)]
    #   or
    result = [''.join([x, y]) for x, y in zip(values[::2], values[1::2])]
    print(result)

values = ['1', '2', '3', '4', '5', '6', '7', '8']
join_list_adjacent(values)

values = ['1', '2', '3']
join_list_adjacent(values)
