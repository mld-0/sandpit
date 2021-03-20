
def last_digit(n):
    n_last = n % 10
    return n_last

def last_digit_product(a, b, c):
    a_last = last_digit(a)
    b_last = last_digit(b)
    c_last = last_digit(c)
    print(str(a_last * b_last)[-1] == str(c_last)[-1])

last_digit_product(12, 22, 44)
last_digit_product(145, 122, 1010)
last_digit_product(0, 22, 40)
last_digit_product(1, 22, 40)
last_digit_product(145, 122, 101)

