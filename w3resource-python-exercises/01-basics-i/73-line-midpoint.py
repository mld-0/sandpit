def midpoint(p1, p2):
    result = []
    for a, b in zip(p1, p2):
        c = (b + a) / 2
        result.append(c)
    print(tuple(result))

p1 = (2, 2)
p2 = (4, 4)
midpoint(p1, p2)
