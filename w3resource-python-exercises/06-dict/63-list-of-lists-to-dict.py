
def list_of_lists_to_dict(values):
    result_dict = {L[0]: [L[1], L[2]] for L in values}
    print(result_dict)

values = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
list_of_lists_to_dict(values)

