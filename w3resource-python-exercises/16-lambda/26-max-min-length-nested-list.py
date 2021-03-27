
max_length_nested_list = lambda x: (len(sorted(x, key=lambda a: len(a), reverse=True)[0]), sorted(x, key=lambda a: len(a), reverse=True)[0])
min_length_nested_list = lambda x: (len(sorted(x, key=lambda a: len(a))[0]), sorted(x, key=lambda a: len(a))[0])

print(max_length_nested_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
print(min_length_nested_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
