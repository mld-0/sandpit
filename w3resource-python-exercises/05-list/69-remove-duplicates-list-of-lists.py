import itertools

def remove_duplicates_list_of_lists(values):
    result = []
    for x in values:
        if x not in result:
            result.append(x)
    result = result
    #   or
    values_sorted = sorted(values)
    result = [x for x, _ in itertools.groupby(values_sorted)]
    print(result)

values = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 
remove_duplicates_list_of_lists(values)
