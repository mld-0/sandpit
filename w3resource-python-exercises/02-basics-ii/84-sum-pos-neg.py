
def sum_pos_neg(values):
    sums = [0, 0]
    for v in values:
        if (v > 0):
            sums[1] += v
        else:
            sums[0] += 1
    print(sums)

sum_pos_neg([1, 2, 3, 4, 5])
sum_pos_neg([-1, -2, -3, -4, -5])
sum_pos_neg([1, 2, 3, -4, -5])
sum_pos_neg([1, 2, -3, -4, -5])
