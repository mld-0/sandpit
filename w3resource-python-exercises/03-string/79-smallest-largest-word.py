import re

def smallest_largest_word(_str):
    _str_words = re.findall('\w+', _str)
    _str_words_sorted = sorted(_str_words, key=lambda x: len(x))
    print(_str_words_sorted[0])
    print(_str_words_sorted[-1])

smallest_largest_word("Write a Java program to sort an array of given integers using Quick sort Algorithm.")
