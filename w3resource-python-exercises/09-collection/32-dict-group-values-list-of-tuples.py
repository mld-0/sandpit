from collections import defaultdict

def dict_group_values_list_of_tuples(values):
    result_dict = defaultdict(list)
    for t in values:
        result_dict[t[0]].append(t[1])
    print(result_dict)

classes = ( ('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1),)
dict_group_values_list_of_tuples(classes)
