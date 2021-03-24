
def sort_by_inner_index(values, n):
    result = sorted(values, key=lambda x: x[n])
    print(result)

values = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

sort_by_inner_index(values, 0)
sort_by_inner_index(values, 2)
