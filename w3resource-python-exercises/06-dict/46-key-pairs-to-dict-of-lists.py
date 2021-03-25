
def key_pairs_to_dict_of_lists(values):
    result_dict = dict()
    for k, v in values:
        if k in result_dict:
            result_dict[k].append(v)
        else:
            result_dict[k] = [v]
    print(result_dict)

values = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
key_pairs_to_dict_of_lists(values)
