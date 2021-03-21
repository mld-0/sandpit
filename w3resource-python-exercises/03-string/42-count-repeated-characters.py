from collections import defaultdict

def count_repeated_characters(_str):
    _str_set = set(_str)
    count_characters = {k: v for k,v in sorted([[k, _str.count(k)] for k in _str_set], key=lambda x: x[1], reverse=True) if v > 1}
    #   or
    count_characters = {k: 0 for k in _str_set}
    for c in _str:
        count_characters[c] += 1
    count_characters = {k: v for k,v in sorted(count_characters.items(), key=lambda x: x[1], reverse=True) if v > 1}

    print(count_characters)

count_repeated_characters('thequickbrownfoxjumpsoverthelazydog')
