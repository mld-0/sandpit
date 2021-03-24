
def flatten_nested_list(values):
    result = []
    for x in values:
        if isinstance(x, list):
            for y in x:
                result.append(y)
        else:
            result.append(x)
    return result

def decode_run_length_encoded(values):
    result = [[x[1]] * x[0] if isinstance(x, list) else x for x in values]
    result = flatten_nested_list(result)
    print(result)

values = [[2, 1], 2, 3, [2, 4], 5, 1] 
decode_run_length_encoded(values)

