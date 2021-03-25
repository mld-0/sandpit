
def merge_dicts(a, b):
    result = dict()
    result.update(a)
    result.update(b)
    print(result)

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
merge_dicts(d1, d2)
