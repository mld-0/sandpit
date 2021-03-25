
def dict_filter_tuple_values(d, f):
    result = {k: v for k, v in d.items() if f(v)}
    print(result)

d = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
f = lambda x: x[0] >= 6 and x[1] >= 70
dict_filter_tuple_values(d, f)
