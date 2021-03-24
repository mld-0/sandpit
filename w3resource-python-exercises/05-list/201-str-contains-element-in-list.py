
def str_contains_element_in_list(_str, values):
    result = any([x in _str for x in values])
    print(result)


_str = 'https://www.w3resource.com/python-exercises/list/'
values = ['.com', '.edu', '.tv']
str_contains_element_in_list(_str, values)

_str = 'https://www.w3resource.net'
values = ['.com', '.edu', '.tv']
str_contains_element_in_list(_str, values)

