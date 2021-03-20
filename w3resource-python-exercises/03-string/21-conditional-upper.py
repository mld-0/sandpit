
def conditional_upper(_str):
    _str_uppers_firstfour = [i for i in range(min(len(_str), 4)) if _str[i].isupper()]
    if len(_str_uppers_firstfour) >= 2:
        print(_str.upper())
    else:
        print(_str)

conditional_upper('Python')
conditional_upper('PyThon')

