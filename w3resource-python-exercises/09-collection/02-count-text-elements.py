from collections import Counter

def count_text_elements(_str):
    _str_counter = Counter(_str)
    print(_str_counter.most_common())

_str = 'lkseropewdssafsdfafkpwe'
count_text_elements(_str)

