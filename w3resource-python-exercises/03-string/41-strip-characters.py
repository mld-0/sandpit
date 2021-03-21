
def strip_characters(_str, _chars):
    _chars_list = list(_chars)
    result_str = ''.join([x for x in _str if not x in _chars_list])
    print(result_str)


strip_characters("The quick brown fox jumps over the lazy dog.", "aeiou")
