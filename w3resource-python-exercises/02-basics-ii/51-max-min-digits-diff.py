def max_min_digits_diff(n):
    n_digits = list(str(n))
    n_digits = [int(x) for x in n_digits]
    n_digits_max = int(''.join([str(x) for x in sorted(n_digits, reverse=True)]))
    n_digits_min = int(''.join([str(x) for x in sorted(n_digits)]))
    delta = n_digits_max - n_digits_min
    print(delta)

max_min_digits_diff(2345)
