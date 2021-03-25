
def dict_sort_list_elements(d):
    result = {k: sorted(v) for k, v in d.items()}
    print(result)

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
dict_sort_list_elements(num)

