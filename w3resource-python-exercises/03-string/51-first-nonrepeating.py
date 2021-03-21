
def first_nonrepeating(_str):
    _str_unique = set(_str)
    _str_count = {k: _str.count(k) for k in _str_unique}
    #print(_str_count)
    for c in _str:
        if _str_count[c] == 1:
            print(c)
            return
    print(None)

first_nonrepeating('abcdef')
first_nonrepeating('abcabcdef')
first_nonrepeating('aabbcc')

