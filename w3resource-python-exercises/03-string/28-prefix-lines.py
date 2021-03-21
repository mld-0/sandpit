import textwrap

sample_text = '''    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.'''

_prefix = '>' * 4
sample_text = textwrap.dedent(sample_text)
sample_text = textwrap.indent(sample_text, prefix=_prefix)
print(sample_text)

