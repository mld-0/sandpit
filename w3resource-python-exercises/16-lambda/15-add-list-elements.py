
a = [1, 2, 3]
b = [4, 5, 6]

add_list_elements = lambda a, b: [i+j for i, j in zip(a, b)]
#   or
add_list_elements = lambda a, b: list(map(lambda i, j: i+j, a, b))

print(add_list_elements(a, b))

