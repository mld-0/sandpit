def pair_odd_product(values):
    pairs = []
    for i in range(len(values)):
        x = values[i]
        for j in range(i, len(values)):
            y = values[j]
            if (x * y % 2 != 0):
                pairs.append([x, y])
    print(pairs)

dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]

pair_odd_product(dt1)
pair_odd_product(dt2)

