
def rev_multi_four(_str):
    if len(_str) % 4 == 0:
        print(_str[::-1])
    else:
        print(_str)

rev_multi_four('abcd')
rev_multi_four('python')
