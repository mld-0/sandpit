
def list_of_tuples_to_dict(values):
    result_dict = dict()
    for x in values:
        if x[0] in result_dict:
            result_dict[x[0]].append(x[1])
        else:
            result_dict[x[0]] = [x[1]]
    #   or
    result_dict = dict()
    for x in values:
        result_dict.setdefault(x[0], []).append(x[1])
    print(result_dict)

t = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
list_of_tuples_to_dict(t)

