import re

def remove_duplicate_words(_str):
    result_list = []
    delim = " "
    _str_words = re.findall('\w+', _str)
    for word in _str_words:
        if word not in result_list:
            result_list.append(word)
    print(delim.join(result_list))

remove_duplicate_words("Python Exercises Practice Solution Exercises")
