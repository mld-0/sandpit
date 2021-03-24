
def remove_list_dict_kv_pairs(values, remove_key):
    result = [{k: v for k, v in d.items() if k != remove_key} for d in values]
    print(result)

original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
remove_list_dict_kv_pairs(original_list, 'key1')

