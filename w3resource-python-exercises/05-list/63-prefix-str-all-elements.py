
def prefix_str_all_elements(values, _str):
    result = [_str + str(x) for x in values]
    print(result)

values = [1, 2, 3, 4]
_str = 'emp'

prefix_str_all_elements(values, _str)
