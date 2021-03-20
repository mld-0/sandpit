from collections import Counter

def count_frequency(_str):
    _str_counter = Counter(_str)
    print(_str_counter)

count_frequency('google.com')
