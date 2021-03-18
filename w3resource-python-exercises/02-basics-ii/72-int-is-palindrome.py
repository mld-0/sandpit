
def int_is_palindrome(value):
    if (value < 0):
        return False
    value_str = str(value)
    if value_str[::-1] == value_str:
        return True
    else:
        return False

print(int_is_palindrome(100))
print(int_is_palindrome(252))
print(int_is_palindrome(-838))

