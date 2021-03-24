import itertools

def n_largest_products(a, b, n):
    ab_products_sorted = sorted([i*j for i, j in itertools.product(a, b)], reverse=True)
    print(ab_products_sorted[:n])

a = [1, 2, 3, 4, 5, 6]
b = [3, 6, 8, 9, 10, 6]

n_largest_products(a, b, 3)
n_largest_products(a, b, 4)

