import re
import collections

input_text = """Thank you for your comment and your participation."""

words = re.findall("\w+", input_text)
words_counter = collections.Counter(words)
words_len = {word: len(word) for word in words}
words_len = {k: v for k, v in sorted(words_len.items(), key=lambda x: x[1], reverse=True)}

most_common_word = words_counter.most_common(1)[0][0]
longest_word = next(iter(words_len))

print(most_common_word)
print(longest_word)



