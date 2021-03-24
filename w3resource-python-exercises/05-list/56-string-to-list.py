
def string_to_list(_str, split_char):
    result = _str.split(split_char)
    print(result)

_str = 'asdf,aqdd,322'
split_char = ','

string_to_list(_str, split_char)

#   Literal list as string, using eval()
color = "['Red', 'Green', 'White']"
result = eval(color)
print(result)

