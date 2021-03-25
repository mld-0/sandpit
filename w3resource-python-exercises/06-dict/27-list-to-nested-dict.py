
def list_to_nested_dict(keys):
    result = loop_d = {}
    for n in num_list:
        loop_d[n] = {}
        loop_d = loop_d[n]
    print(result)

num_list = [1, 2, 3, 4]
list_to_nested_dict(num_list)

