import itertools

def largest_three_product(values):
    values_combinations = itertools.combinations(values, 3)
    values_products = [a * b * c for a, b, c in values_combinations]
    values_products_sorted = sorted(values_products)
    print(values_products_sorted[-1])

largest_three_product([-10, -20, 20, 1])
largest_three_product([-1, -1, 4, 2, 1])
largest_three_product([1, 2, 3, 4, 5, 6])
