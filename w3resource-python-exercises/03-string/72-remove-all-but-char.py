
def remove_all_but_char(_str, c):
    result = ''.join([x for x in _str if x == c])
    print(result)

remove_all_but_char("Python Exercises", 'P')
remove_all_but_char("google", 'g')
remove_all_but_char("exercises", 'e')
