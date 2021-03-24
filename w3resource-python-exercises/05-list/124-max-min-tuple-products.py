
def max_min_tuple_products(values):
    pass
    values_products = [x*y for x,y in values]
    _max_min_product = (max(values_products), min(values_products))
    print(_max_min_product)

values = [(2, 7), (2, 6), (1, 8), (4, 9)]
max_min_tuple_products(values)

