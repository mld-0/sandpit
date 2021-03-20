
def is_narcissistic_number(n):
    n_str = str(n)
    n_str_sum = sum([int(x) ** len(n_str) for x in n_str])
    if int(n_str_sum) == n:
        print(True)
    else:
        print(False)

is_narcissistic_number(153)
is_narcissistic_number(370)
is_narcissistic_number(407)
is_narcissistic_number(409)
is_narcissistic_number(1634)
is_narcissistic_number(8208)
is_narcissistic_number(9474)
is_narcissistic_number(9475)
