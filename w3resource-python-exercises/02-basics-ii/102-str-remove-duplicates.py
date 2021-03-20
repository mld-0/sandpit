
def str_remove_duplicates(_str):
    """Remove consecutive duplicate letters in string."""
    result = _str[0]
    for c in _str[1:]:
        if len(result) > 0 and not c == result[-1]:
            result += c
    print(result)

str_remove_duplicates("PPYYYTTHON")
str_remove_duplicates("PPyyythonnn")
str_remove_duplicates("Java")
str_remove_duplicates("PPPHHHPPP")
