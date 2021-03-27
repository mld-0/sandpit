import bisect

values = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
values_sorted = []

print(values)

for n in values:
    bisect.insort(values_sorted, n)

print(values_sorted)
