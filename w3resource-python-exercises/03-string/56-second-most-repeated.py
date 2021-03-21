import re
from collections import Counter

def second_most_repeated(_str):
    _str_words = re.findall('\w+', _str)
    unique_words = set(_str_words)
    count_words = Counter(_str_words)
    print(list(count_words.items())[1])

second_most_repeated("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster.")

