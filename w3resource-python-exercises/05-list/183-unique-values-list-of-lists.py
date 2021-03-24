
def unique_values_list_of_lists(values):
    unique_values = set()
    for L in values:
        for x in L:
            unique_values.add(x)
    print(list(unique_values))
        

values = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
unique_values_list_of_lists(values)

values = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
unique_values_list_of_lists(values)

