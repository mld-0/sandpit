
def first_last_two(_str):
    if len(_str) < 2:
        print('')
        return
    print(_str[:2] + _str[-2:])

first_last_two('w3resource')
first_last_two('w3')
first_last_two('w')
