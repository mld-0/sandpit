
def dict_kv_pairs_intersection(a, b):
    a_and_b = set(a.items()) & set(b.items())
    print(a_and_b)


a = {'key1': 1, 'key2': 3, 'key3': 2} 
b = {'key1': 1, 'key2': 2}
dict_kv_pairs_intersection(a, b)
