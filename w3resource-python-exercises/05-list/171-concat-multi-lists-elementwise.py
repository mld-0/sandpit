import itertools

def concat_multi_list_elementwise(*values):
    result = []
    for L in itertools.zip_longest(*values, fillvalue=''):
        loop_x = ''.join(L)
        result.append(loop_x)
    print(result)

a = ['0', '1', '2', '3', '4']
b = ['red', 'green', 'black', 'blue', 'white']
c = ['100', '200', '300', '400', '500']
concat_multi_list_elementwise(a, b, c)

