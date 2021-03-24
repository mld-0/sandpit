
def print_space_seperated(values):
    _sep = ' '
    result = _sep.join([str(x) for x in values])
    print(result)

num = [1, 2, 3, 4, 5]
print_space_seperated(num)

