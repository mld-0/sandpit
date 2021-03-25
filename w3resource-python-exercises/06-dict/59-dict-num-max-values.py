
def dict_num_max_values(d, n):
    d_sorted = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    d_sorted_keys = list(d_sorted.keys())
    print(d_sorted_keys[:n])


d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
dict_num_max_values(d, 1)
dict_num_max_values(d, 2)
dict_num_max_values(d, 5)
