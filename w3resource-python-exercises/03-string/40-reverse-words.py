import re

def reverse_words(_str):
    words_list = re.findall('\w+', _str)
    words_list_reversed = list(reversed(words_list))
    print(words_list_reversed)


reverse_words("The quick brown fox jumps over the lazy dog.")
reverse_words("Python Exercises")

