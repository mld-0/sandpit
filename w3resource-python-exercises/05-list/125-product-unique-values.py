import functools
import operator

def product_unique_values(values):
    unique_values = list(set(values))
    product = 1
    for x in unique_values:
        product *= x
    #   or
    product = functools.reduce(operator.mul, unique_values)
    print(product)

values = [10, 20, 30, 40, 20, 50, 60, 40]
product_unique_values(values)
