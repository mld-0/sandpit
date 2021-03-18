import re

def sum_values(_str):
    _str_ints = [int(x) for x in re.findall("[0-9]+", _str)]
    #_str_ints = [int(result.group()) for result in re.finditer("[0-9]+", _str)]
    #print(_str_ints)
    _str_sum = sum(_str_ints)
    print(_str_sum)

sum_values("sd1fdsfs23 dssd56")
sum_values("15apple2banana")
sum_values("flowers5fruit5")
