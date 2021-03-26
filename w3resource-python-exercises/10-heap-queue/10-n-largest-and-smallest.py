import heapq
from pprint import pprint

def n_largest_and_smallest(values, n):
    n_largest = heapq.nlargest(n, values, key=lambda x: x['price'])
    n_smallest= heapq.nsmallest(n, values, key=lambda x: x['price'])
    print(n_largest)
    print(n_smallest)

items = [ {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}, {'name': 'Item-4', 'price': 22.75}, {'name': 'Item-5', 'price': 16.30}, {'name': 'Item-6', 'price': 110.65} ]

n_largest_and_smallest(items, 3)

