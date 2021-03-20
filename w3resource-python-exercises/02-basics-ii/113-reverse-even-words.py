import re

def reverse_even_words(sentance):
    words = re.split('\s+', sentance)
    words_reverse_even = [x[::-1] if len(x) % 2 == 0 else x for x in words]
    print(words_reverse_even)

reverse_even_words("The quick brown fox jumps over the lazy dog")
reverse_even_words("Python Exercises")
