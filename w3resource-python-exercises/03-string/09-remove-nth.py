
def remove_nth(_str, n):
    result = _str[0:n] + _str[n+1:]
    print(result)

remove_nth('Python', 0)
remove_nth('Python', 3)
remove_nth('Python', 5)
