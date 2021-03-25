import itertools

def dict_key_value_combinations(d):
    d_items = d.items()
    #print(d_items)
    d_combinations = list(itertools.combinations(d_items, 2))
    #print(d_combinations)
    d_combinations_mapdict = list(map(dict, d_combinations))
    print(d_combinations_mapdict)

d = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dict_key_value_combinations(d)

d = {'V': [1, 3, 5], 'VI': [1, 5]}
dict_key_value_combinations(d)

