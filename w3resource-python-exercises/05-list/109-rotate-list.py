
def rotate_list(values, n, LR):
    result = []
    if (LR == 'L'):
        result = values[n:] + values[:n]
    elif (LR == 'R'):
        result = values[-n:] + values[:-n]
    else:
        raise Exception("L or R only")
    print(result)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = 4
LR = 'L'
rotate_list(values, n, LR)
n = 2
LR = 'L'
rotate_list(values, n, LR)

n = 4
LR = 'R'
rotate_list(values, n, LR)
n = 2
LR = 'R'
rotate_list(values, n, LR)


