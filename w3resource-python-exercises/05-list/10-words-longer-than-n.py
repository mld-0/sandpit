import re

def words_longer_than_n(_str, n):
    _str_words = [x for x in re.findall('\w+', _str) if len(x) > n]
    print(_str_words)


words_longer_than_n("The quick brown fox jumps over the lazy dog", 3)
