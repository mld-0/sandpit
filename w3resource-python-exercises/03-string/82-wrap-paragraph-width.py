import textwrap

def wrap_paragraph_width(_str, width): 
    result = textwrap.fill(_str, width)
    print(result)

wrap_paragraph_width("The quick brown fox.", 10)
