
def remove_empty_lists(values):
    result = [x for x in values if x != []]
    print(result)

values = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
remove_empty_lists(values)
