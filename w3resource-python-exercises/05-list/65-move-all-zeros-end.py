
def move_all_zeros_end(values):
    result = []
    zeros = []
    for x in values:
        if x == 0:
            zeros.append(x)
        else:
            result.append(x)
    result = result + zeros
    #   or
    result = sorted(values, key=lambda x: x == 0)
    print(result)

values = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
move_all_zeros_end(values)
        
