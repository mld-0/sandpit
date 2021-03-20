
def caesar_cipher_map(start, end, n):
    Chars = [chr(x) for x in range(ord(start), ord(end)+1)]
    chars_map = dict()
    for i in range(len(Chars)):
        loop_from = Chars[i]
        loop_to_index = i + n
        if (loop_to_index >= len(Chars)):
            loop_to_index = i + n - len(Chars)
        loop_to = Chars[loop_to_index]
        chars_map[loop_from] = loop_to
    return chars_map

def caesar_cipher(_str, n):
    uppers_map = caesar_cipher_map('A', 'Z', n)
    lowers_map = caesar_cipher_map('a', 'z', n)
    result = ""
    for v in _str:
        if v in uppers_map.keys():
            result += uppers_map[v]
        elif v in lowers_map.keys():
            result += lowers_map[v]
        else:
            result += v
    return result

_str = 'abc'
result = caesar_cipher(_str, 2)
print(result)

result = caesar_cipher(result, -2)
print(result)

