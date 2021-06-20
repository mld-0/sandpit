#!/usr/env/bin python3
import sys

print("Enter words, one-per-line, then <C-d>:")

input_words = []
for line in sys.stdin:
    input_words.append(line.strip())

print("input_words=(%s)" % input_words)

#   By intializing all keys with zero value
words_counter = dict.fromkeys(set(input_words), 0)
for loop_word in input_words:
    words_counter[loop_word] += 1

#   By initalizing each key with zero value
words_counter = {}
for loop_word in input_words:
    if not loop_word in words_counter.keys():
        words_counter[loop_word] = 0
    words_counter[loop_word] += 1

#   Using dict.get() with default zero
words_counter = {}
for loop_word in input_words:
    words_counter[loop_word] = words_counter.get(loop_word, 0) + 1

#   Using collections.defaultdict with int for default zero
from collections import defaultdict
words_counter = defaultdict(int)
for loop_word in input_words:
    words_counter[loop_word] += 1

#   Using collections.Counter
from collections import Counter
words_counter = Counter(input_words)

#   Print result:
for k, v in words_counter.items():
    print("k=(%s), v=(%s)" % (k, v))

