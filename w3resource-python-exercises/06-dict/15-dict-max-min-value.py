
def dict_max_min_value(d):
    d_sorted = dict(sorted(d.items(), key=lambda x: x[1]))
    print(list(d_sorted.items())[-1])
    print(list(d_sorted.items())[0])

my_dict = {'x':500, 'y':5874, 'z': 560}
dict_max_min_value(my_dict)
