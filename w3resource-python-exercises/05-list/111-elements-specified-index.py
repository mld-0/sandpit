
def items_specified_index(values, indexes):
    results = [x for i, x in enumerate(values) if i in indexes]
    print(results)
    
values = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
indexes = [0, 3, 5, 7, 10]
items_specified_index(values, indexes)
