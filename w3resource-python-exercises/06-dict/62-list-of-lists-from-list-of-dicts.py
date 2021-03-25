
def list_of_lists_from_list_of_dicts(values):
    result_list = [[v for k,v in d.items()] for d in values]
    print(result_list)


values = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
list_of_lists_from_list_of_dicts(values)

