
def dict_drop_empty(d):
    result = {k:v for k, v in d.items() if v is not None}
    print(result)

d = {'c1': 'Red', 'c2': 'Green', 'c3': None}
dict_drop_empty(d)

