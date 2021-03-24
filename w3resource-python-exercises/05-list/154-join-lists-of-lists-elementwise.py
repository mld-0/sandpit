
def join_list_of_lists_elementwise(a, b):
    result = []
    for aa, bb in zip(a, b):
        result_loop = []
        for x in aa:
            result_loop.append(x)
        for y in bb:
            result_loop.append(y)
        result.append(result_loop)
    print(result)

a = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
join_list_of_lists_elementwise(a, b)

a = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
b = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
join_list_of_lists_elementwise(a, b)
