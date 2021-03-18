
def matrix_print_alternating(values):
    flip = False
    for loop_row in values:
        if flip:
            loop_row.reverse()
        flip = not flip
        for loop_v in loop_row:
            print(loop_v)

values = [[1, 2, 3,4], [5, 6, 7, 8], [0, 6, 2, 8], [2, 3, 0, 2]]
matrix_print_alternating(values)
