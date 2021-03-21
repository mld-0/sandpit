
def contains_alphabet(_str):
    alphabet = set([chr(x) for x in range(ord('a'), ord('z')+1)])
    _str_lower_set = set(_str.lower())
    print(_str_lower_set >= alphabet)

contains_alphabet('The quick brown fox jumps over the lazy dog')
contains_alphabet('The quick brown fox jumps over the lazy cat')
