
def sort_csv_words(_str):
    _str_split = set([x.strip() for x in _str.split(',')])
    _str_split_sorted = sorted(list(_str_split))
    print(_str_split_sorted)

sort_csv_words('red, white, black, red, green, black')
