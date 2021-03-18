import re

def string_decompress(_str):
    result_str = ""
    _str_split = re.split(r'#[0-9]', _str)
    _str_nums = [int(x.groups()[0]) for x in re.finditer(r'#(?P<num>[0-9])', _str)]
    result_str += _str_split[0]
    for loop_split, loop_num in zip(_str_split[1:], _str_nums):
        result_str += loop_split[0] * loop_num
        result_str += loop_split[1:]
    print(result_str)


_str = "XY#6Z1#4023"
string_decompress(_str)

_str = "#39+1=1#30"
string_decompress(_str)
