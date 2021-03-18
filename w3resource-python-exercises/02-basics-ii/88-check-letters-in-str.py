
def check_letters_in_str(a, b):
    result = True
    b_letters = set(b)
    for loop_b in b_letters:
        if not loop_b in a:
            result = False
    print(result)

check_letters_in_str(*["python", "ypth"])
check_letters_in_str(*["python", "ypths"])
check_letters_in_str(*["python", "ypthon"])
check_letters_in_str(*["123456", "01234"])
check_letters_in_str(*["123456", "1234"])

