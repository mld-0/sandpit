
def dict_is_empty(d):
    result = len(d)
    print(result == 0)

d = dict()
dict_is_empty(d)

d = dict({1: 'a'})
dict_is_empty(d)
