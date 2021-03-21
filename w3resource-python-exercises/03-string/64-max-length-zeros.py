import re

def max_length_zeros(_str):
    _str_zeros = re.findall('0+', _str)
    _str_zeros_len = [len(x) for x in _str_zeros]
    max_zeros_len = max(_str_zeros_len)
    print(max_zeros_len)

max_length_zeros('111000010000110')
max_length_zeros('111000111')

