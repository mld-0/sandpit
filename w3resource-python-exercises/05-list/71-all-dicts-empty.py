
def all_dicts_empty(values):
    result = all([len(x) == 0 for x in values])
    print(result)

values = [{}, {}, {}]
all_dicts_empty(values)

values = [{1:2}, {}, {}]
all_dicts_empty(values)

