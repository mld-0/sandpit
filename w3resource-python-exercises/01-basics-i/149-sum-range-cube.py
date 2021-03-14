def sum_range_cube(value):
    _sum = 0
    for n in range(value - 1, 0, -1):
        _sum += n ** 3
    print(_sum)

value = 6
sum_range_cube(value)

