import collections


def merge_two_dicts(a, b):
    result_dict = dict(collections.ChainMap({}, b, a))
    #   or
    result_dict = {**a, **b}
    #   or
    result_dict = a | b  # python 3.9+
    print(result_dict)

def merge_dicts(*values):
    result_dict = dict()
    for x in values:
        result_dict = {**result_dict, **x} 
    print(result_dict)

a = {'R': 'Red', 'B': 'Black', 'P': 'Pink'} 
b = {'G': 'Green', 'W': 'White'}
merge_dicts(a, b)

a = {'R': 'Red', 'B': 'Black', 'P': 'Pink'} 
b = {'G': 'Green', 'W': 'White'} 
c = {'O': 'Orange', 'W': 'White', 'B': 'Black'}
merge_dicts(a, b, c)


