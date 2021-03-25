
def dict_key_value_parings(d):
    result_dict = {k: c for k,v in d.items() for c in v}
    print(result_dict)

d = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
dict_key_value_parings(d)
