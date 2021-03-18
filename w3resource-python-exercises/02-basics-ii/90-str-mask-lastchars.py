
def str_mask_lastchars(_str):
    result = "*" * (len(_str) - 5) + _str[-5:]
    print(result)

str_mask_lastchars("kdi39323swe")
str_mask_lastchars("12345abcdef")
str_mask_lastchars("12345")
