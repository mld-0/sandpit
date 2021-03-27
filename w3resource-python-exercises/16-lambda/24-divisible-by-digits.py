
div_by_digits = lambda x: all([int(n) != 0 and x % int(n) == 0 for n in str(x)])
divisible_by_digits = lambda n: [a for a in range(1, n) if div_by_digits(a)]

print(divisible_by_digits(23))

