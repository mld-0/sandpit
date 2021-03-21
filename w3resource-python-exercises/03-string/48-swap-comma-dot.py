
def swap_comma_dot(_str):
    result = ""
    for c in _str:
        if c == ',':
            result += '.'
        elif c == '.':
            result += ','
        else:
            result += c
    print(result)

#   or

def swap_comma_dot_alt(_str):
    _trans = _str.maketrans
    result = _str.translate(_trans(',.', '.,'))
    print(result)

swap_comma_dot("32.054,23")
swap_comma_dot_alt("32.054,23")

