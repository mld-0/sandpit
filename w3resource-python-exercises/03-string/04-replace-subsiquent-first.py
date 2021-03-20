
def replace_subsiquent_first(_str):
    first_char = _str[0]
    while (first_char in _str):
        _str = _str.replace(first_char, '$')
    _str = first_char + _str[1:]
    print(_str)

replace_subsiquent_first('restart')
