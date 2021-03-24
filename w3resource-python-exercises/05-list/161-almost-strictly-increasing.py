
def almost_strictly_increasing(values):
    if len(values) == 0:
        print(True)
        return
    out_of_order_count = 0
    for i in range(1, len(values)):
        loop_max = sorted(values[:i], reverse=True)
        if len(loop_max) > 1:
            loop_max = loop_max[1]
        else:
            loop_max = loop_max[0]

        if values[i] < loop_max:
            out_of_order_count += 1
    print(out_of_order_count <= 1)

almost_strictly_increasing([])
almost_strictly_increasing([1])
almost_strictly_increasing([1, 2])
almost_strictly_increasing([1, 2, 3])
almost_strictly_increasing([3, 1, 2])
almost_strictly_increasing([1, 2, 3, 0, 4, 5, 6])
almost_strictly_increasing([1, 2, 3, 0])
almost_strictly_increasing([1, 2, 0, 3])
almost_strictly_increasing([10, 1, 2, 3, 4, 5])
almost_strictly_increasing([1, 2, 10, 3, 4])
almost_strictly_increasing([1, 2, 3, 12, 4, 5])

almost_strictly_increasing([3, 2, 1])
almost_strictly_increasing([1, 2, 0, -1])
almost_strictly_increasing([5, 6, 1, 2])
almost_strictly_increasing([1, 2, 3, 0, -1])
almost_strictly_increasing([10, 11, 12, 2, 3, 4, 5]) 

