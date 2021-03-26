from collections import Counter
import re

def count_words(text):
    words = re.findall('\w+', text)
    words_counter = Counter(words)
    print(words_counter.most_common(10))

text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""

count_words(text)
