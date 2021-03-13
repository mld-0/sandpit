def check_if(a, b):
    if (a == b):
        return True
    if (a + b == 5):
        return True
    if (abs(a - b) == 5):
        return True
    return False

print(check_if(7, 2))
print(check_if(3, 2))
print(check_if(2, 2))
