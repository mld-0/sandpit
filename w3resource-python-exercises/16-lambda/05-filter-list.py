
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

values_even = list(filter(lambda x: x%2==0, values))
values_odd = list(filter(lambda x: x%2!=0, values))

print(values_even)
print(values_odd)
