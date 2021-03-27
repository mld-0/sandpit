
array_intersection = lambda a, b: [x for x in set([*a, *b]) if (x in a and x in b)]

a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]

print(array_intersection(a, b))

