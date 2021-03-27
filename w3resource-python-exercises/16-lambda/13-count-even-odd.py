
count_even = lambda x: sum([1 for n in x if n % 2 == 0])
count_odd = lambda x: sum([1 for n in x if n % 2 != 0])

values = [1, 2, 3, 5, 7, 8, 9, 10]

print(count_even(values))
print(count_odd(values))


