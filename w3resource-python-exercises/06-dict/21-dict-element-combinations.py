import itertools

def dict_element_combinations(d):
    result = [''.join(x) for x in itertools.product(*d.values())]
    print(result)

d = {'1':['a','b'], '2':['c','d']}
dict_element_combinations(d)
