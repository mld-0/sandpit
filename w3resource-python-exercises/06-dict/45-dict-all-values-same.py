
def dict_all_values_same(d):
    values_set = set(d.values())
    print(len(values_set) == 1)

d = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
dict_all_values_same(d)
