import re

def substring_index(_str, substr):
    result_finditer = re.finditer(substr, _str)
    result_startandend = [[x.start(), x.end()] for x in result_finditer]
    if len(result_startandend) == 0:
        print(None)
        return
    print(result_startandend[0][0])

substring_index("Python Exercises", "Ex")
substring_index("Python Exercises", "yt")
substring_index("Python Exercises", "PY")
