
def swap_cases(_str):
    result = ""
    for c in _str:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    print(result)

swap_cases("Python Exercises")
swap_cases("Java")
swap_cases("NumPy")
