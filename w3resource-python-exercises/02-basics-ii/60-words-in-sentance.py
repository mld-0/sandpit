import re

def words_in_sentance(var_str):
    length_range = (3, 6)
    var_words = [x for x in re.findall('\w*', var_str) if len(x) >= length_range[0] and len(x) <= length_range[1]]
    words_lengths = [len(x) for x in var_words]
    print(var_words)
    print(words_lengths)

var_str = "The quick brown fox"
words_in_sentance(var_str)
