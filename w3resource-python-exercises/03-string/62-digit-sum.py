
def sum_digits_string(_str):
    result = 0
    digits = [chr(x) for x in range(ord('0'), ord('9')+1)]
    for c in _str:
        if c in digits:
            result += int(c)
    print(result)

sum_digits_string("123abcd45")
sum_digits_string("abcd1234")
