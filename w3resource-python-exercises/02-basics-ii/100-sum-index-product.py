
def sum_index_product(values):
    """Compute sum of each value multipled by its index."""
    if len(values) == 0:
        print(0)
        return
    result = 0
    for i, v in enumerate(values):
        result += i * v
    print(result)

sum_index_product([1,2,3,4])
sum_index_product([-1,-2,-3,-4])
sum_index_product([])
