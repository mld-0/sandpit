def print_details(personal_details):
    result_str = ""
    for k, v in personal_details.items():
        result_str += "%s: %s, " % (k, v)
    print(result_str[:-2])

personal_details = {'name': "Larry", 'age': 14, 'address': "10 Downing Street"}
print_details(personal_details)
