from collections import OrderedDict
import re

def remove_duplicate_words(_str):
    _str_words = re.findall('\w+', _str)
    dict_words = OrderedDict()  # use OrderedDict as set -> set key, disregard value
    for word in _str_words:
        dict_words[word] = None
    result_words = ' '.join(dict_words.keys())
    print(result_words)

_str = 'Python Exercises Practice Solution Exercises'
remove_duplicate_words(_str)
