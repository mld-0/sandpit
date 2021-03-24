
def swap_values(values):
    result = []
    for i in range(0, len(values), 2):
        j = i + 1
        values[i], values[j] = values[j], values[i]
    print(values)

values = [0,1,2,3,4,5]
swap_values(values)
