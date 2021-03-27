
values = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]

second_lowest = lambda x: sorted(x, key=lambda a: a[1], reverse=True)[1]

print(second_lowest(values))
