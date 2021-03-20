import re

def str_second_occurence(_str, search):
    re_result = re.finditer(search, _str)
    result_str, result_start = zip(*[[x.group(), x.start()] for x in re_result])
    if len(result_start) >= 2:
        print(result_start[1])
    else:
        print(-1)

str_second_occurence("The quick brown fox jumps over the lazy dog", "the")
str_second_occurence("the quick brown fox jumps over the lazy dog", "the")
