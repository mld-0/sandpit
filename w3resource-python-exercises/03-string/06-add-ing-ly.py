
def add_ing_ly(_str):
    if len(_str) < 3:
        print(_str)
        return
    if _str.endswith('ing'):
        _str = _str + 'ly'
    else:
        _str = _str + 'ing'
    print(_str)

add_ing_ly('ab')
add_ing_ly('abc')
add_ing_ly('string')
