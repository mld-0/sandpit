
#   Behaviour in case of odd-length _str_outer?
def insert_string_middle(_str_outer, _str_inner):
    result = _str_outer[0:len(_str_outer)//2] + _str_inner + _str_outer[len(_str_outer)//2:]
    print(result)

insert_string_middle('[[]]', 'Python')
insert_string_middle('{{}}', 'PHP')
