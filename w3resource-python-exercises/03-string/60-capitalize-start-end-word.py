import re

def capitalize_start_end_word(_str):
    result = ""
    find_words = re.finditer('\w+', _str)
    words_start_end = [[x.start(), x.end()] for x in find_words]
    for start, end in words_start_end:
        result += _str[start].upper()
        result += _str[start+1:end-1]
        result += _str[end-1].upper()
        if (end < len(_str)):
            result += _str[end]
    print(result)

capitalize_start_end_word("python exercises practice solution")
capitalize_start_end_word("w3resource")

