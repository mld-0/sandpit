from difflib import SequenceMatcher

def string_similarity(a, b):
    a = a.lower()
    b = b.lower()
    seqmatch = SequenceMatcher(None, a, b)
    _ratio = seqmatch.ratio()
    print(_ratio)


a = "Python Exercises"
b = "Python Exercises"
string_similarity(a, b)

a = "Python Exercises"
b = "Python Exercise"
string_similarity(a, b)

a = "Python Exercises"
b = "Python Ex."
string_similarity(a, b)

a = "Python Exercises"
b = "Python"
string_similarity(a, b)

a = "Java Exercises"
b = "Python"
string_similarity(a, b)

