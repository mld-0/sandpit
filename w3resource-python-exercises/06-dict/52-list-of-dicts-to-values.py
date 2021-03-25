
def list_of_dicts_to_values(values):
    result_dict = {}
    for L in values:
        for k, v in L.items():
            if not k in result_dict:
                result_dict[k] = [v]
            else:
                result_dict[k].append(v)
    result_values = [[x for x in result_dict[k]] for k in result_dict.keys()]
    print(result_values)
    #   or
    result_values = list(zip(*[[x for x in d.values()] for d in values]))
    print(result_values)
            
values = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
list_of_dicts_to_values(values)
