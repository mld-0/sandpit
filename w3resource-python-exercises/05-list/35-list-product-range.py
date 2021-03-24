import itertools
import functools

def list_product_range(values, n):
    result = [v+str(i) for i in range(1, n+1) for v in values]
    #   or
    result = list(itertools.starmap(lambda x,y: x+str(y), itertools.product(values, range(1, n+1))))
    print(result)

list_product_range(['p', 'q'], 5)
