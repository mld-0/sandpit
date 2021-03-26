from collections import OrderedDict

def ordereddict_from_dict(d):
    result_d = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
    result_d_rev = OrderedDict(reversed(result_d.items()))
    for k, v in result_d_rev.items():
        print(k, v)

d = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
ordereddict_from_dict(d)

