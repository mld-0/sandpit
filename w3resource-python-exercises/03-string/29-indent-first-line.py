import textwrap

sample_text = '''Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.'''

sample_text = textwrap.fill(sample_text, initial_indent='>'*4, subsequent_indent='', width=80)
print(sample_text)

