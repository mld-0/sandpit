
def sort_list_nested_dicts(values):
    result = []
    result = sorted(values, key=lambda x: x['key']['subkey'])

    print(result)

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
sort_list_nested_dicts(my_list)

