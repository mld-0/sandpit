
def remove_specific_elements(values):
    _remove_index = [0, 4, 5]
    result = []
    for i, n in enumerate(values):
        if not i in _remove_index:
            result.append(n)
    print(result)

remove_specific_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
