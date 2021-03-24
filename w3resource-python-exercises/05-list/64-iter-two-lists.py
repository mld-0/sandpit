
def iter_two_lists(a, b):
    for loop_a, loop_b in zip(a, b):
        print(loop_a, loop_b)

a = [1, 2, 3]
b = ['a', 'b', 'c']

iter_two_lists(a, b)
