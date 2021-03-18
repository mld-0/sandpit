
def is_isogram(_str):
    _str_chars = [x for x in _str]
    _str_chars_set = set(_str_chars)
    print(len(_str_chars) == len(_str_chars_set))

is_isogram("w3resource")
is_isogram("w3r")
is_isogram("Python")
is_isogram("Java")

