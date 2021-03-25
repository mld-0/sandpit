
def dict_of_lists_to_list_of_dicts(d):
    result_list = []
    result_keys = d.keys()
    result_values = d.values()

    for V in zip(*result_values):
        loop_dict = dict()
        for k, v in zip(result_keys, V):
            loop_dict[k] = v
        result_list.append(loop_dict)
    #   or
    result_list = [{k: [v for v in V]} for k, V in d.items()]

    print(result_list)


d = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
dict_of_lists_to_list_of_dicts(d)
