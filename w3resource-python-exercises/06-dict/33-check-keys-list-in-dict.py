
def check_keys_list_in_dict(d, values):
    result = d.keys() >= values
    print(result)

students = { 'name': 'Alex', 'class': 'V', 'roll_id': '2' }

values = {'class', 'name'}
check_keys_list_in_dict(students, values)

values = {'name', 'Alex'}
check_keys_list_in_dict(students, values)

values = {'roll_id', 'name'}
check_keys_list_in_dict(students, values)


