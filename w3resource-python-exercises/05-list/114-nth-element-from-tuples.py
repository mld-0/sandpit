
def nth_element_from_tuples(values, n):
    result = [x[n] for x in values]
    print(result)

values = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

n = 0
nth_element_from_tuples(values, n)

n = 2
nth_element_from_tuples(values, n)
