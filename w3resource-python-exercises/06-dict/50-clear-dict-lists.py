
def clear_dict_lists(d):
    result_dict = dict(d)
    for k in result_dict.keys():
        result_dict[k] = []
    print(result_dict)

d = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
clear_dict_lists(d)
