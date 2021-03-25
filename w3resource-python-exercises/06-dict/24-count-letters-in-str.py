from collections import Counter

def count_letters_in_str(_str):
    result = Counter(_str)
    print(dict(result))

_str = 'w3resource'
count_letters_in_str(_str)

