
def move_spaces_front(_str):
    _str = ' ' * _str.count(' ') + _str.replace(' ', '')
    print(_str)

move_spaces_front("w3resource .  com  ")
move_spaces_front("   w3resource.com  ")

