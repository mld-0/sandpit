import itertools

def permutations_n(_str, n):
    _str_list = list(_str)
    result = [''.join(x) for x in itertools.permutations(_str_list, n)]
    print(result)

permutations_n('xyz', 3)
permutations_n('xyz', 2)
permutations_n('abcd', 4)


    
