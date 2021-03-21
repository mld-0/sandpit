
def delete_char_occurences(_str, char_del):
    result = ""
    for c in _str:
        if c != char_del:
            result += c
    print(result)

delete_char_occurences("Delete all occurrences of a specified character in a given string", "a")
