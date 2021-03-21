
def alphabet_position(_str):
    result_count = 0
    _str = _str.lower()
    alphabet = {chr(ord('a')+i): i for i in range(26)}
    for i, c in enumerate(_str):
        if alphabet[c] == i:
            result_count += 1
    print(result_count)

alphabet_position("xbcefg")

