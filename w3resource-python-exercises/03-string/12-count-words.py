import re
from collections import Counter

def word_count(_str):
    str_words = re.findall('\w+', _str)
    str_words_count = Counter(str_words)
    print(dict(str_words_count))

word_count('the quick brown fox jumps over the lazy dog.')
