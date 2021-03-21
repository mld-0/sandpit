
def remove_duplicate_chars(_str):
    result = ""
    for c in _str:
        if not c in result:
            result += c
    print(result)

remove_duplicate_chars("python exercises practice solution")
remove_duplicate_chars("w3resource")
