from collections import defaultdict

def group_kv_pairs_dict_of_lists(values):
    result_dict = defaultdict(list)
    for t in values:
        k, v = t[0], t[1]
        result_dict[k].append(v)
    print(dict(result_dict))

class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
group_kv_pairs_dict_of_lists(class_roll)

