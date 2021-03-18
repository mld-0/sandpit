
def sum_lowest_three(values):
    values_positive = [x for x in values if x > 0]
    values_positive_sorted = sorted(values_positive)
    a, b, c = values_positive_sorted[0:3]
    _sum = a + b + c
    print(_sum)

sum_lowest_three([10, 20, 30, 40, 50, 60, 7])
sum_lowest_three([1, 2, 3, 4, 5])
sum_lowest_three([0, 1, 2, 3, 4, 5])
