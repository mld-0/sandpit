import itertools

def remove_consecutive_duplicates(_str):
    result = ""
    for c in _str:
        if len(result) == 0 or result[-1] != c:
            result += c
    #   or
    result = ""
    for k, v in itertools.groupby(_str):
        result += k
    print(result)

remove_consecutive_duplicates('xxxxyyyyyyy')
remove_consecutive_duplicates('aaaaebbbb')
