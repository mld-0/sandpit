
def access_item_in_dict_value_list(d):
    results = []
    for k, v in d.items():
        results.append(v[4])
    print(results)


d = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19], 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29], 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
access_item_in_dict_value_list(d)
