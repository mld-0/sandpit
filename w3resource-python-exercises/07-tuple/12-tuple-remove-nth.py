
def tuple_remove_nth(t, n):
    result = t[:n] + t[n+1:]
    print(result)

t = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
tuple_remove_nth(t, 1)
