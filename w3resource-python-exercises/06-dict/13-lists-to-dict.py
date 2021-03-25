
def lists_to_dict(a, b):
    d = dict(zip(a, b))
    print(d)

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
lists_to_dict(keys, values)
