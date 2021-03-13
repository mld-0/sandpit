def point_distance(p1, p2):
    result = 0
    for a, b in zip(p1, p2):
        result += (a - b) ** 2
    result = result ** 0.5
    print(result)

p1 = (4, 0)
p2 = (6, 6)
point_distance(p1, p2)

