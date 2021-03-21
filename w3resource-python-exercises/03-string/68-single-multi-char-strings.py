from collections import Counter

def single_multi_char_strings(_str):
    result_single = ""
    result_multi = ""

    _str_char_count = Counter(_str)

    for c in _str:
        if _str_char_count[c] > 1:
            if c not in result_multi:
                result_multi += c
        else:
            result_single += c

    print(result_single)
    print(result_multi)


single_multi_char_strings("aabbcceffgh")
