from collections import Counter

def combine_dicts_add_common(a, b):
    result = dict(a)
    for k, v in b.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v
    #   or
    result = dict(Counter(a) + Counter(b))
    print(result)

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
combine_dicts_add_common(d1, d2)
