
def dict_filter_by_value(d):
    result = {k:v for k,v in d.items() if v > 170}
    print(result)

d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
dict_filter_by_value(d)
