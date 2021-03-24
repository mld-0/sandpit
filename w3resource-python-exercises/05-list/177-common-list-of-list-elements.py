
def common_list_of_list_elements(values):
    common_elements = set(values[0])
    for x in values[1:]:
        common_elements &= set(x)
    result = list(common_elements)
    print(result)

values = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
common_list_of_list_elements(values)

values = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
common_list_of_list_elements(values)

