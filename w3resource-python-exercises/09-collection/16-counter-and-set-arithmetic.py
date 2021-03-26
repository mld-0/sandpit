import collections

c1 = collections.Counter([1, 2, 3, 4, 5])
c2 = collections.Counter([4, 5, 6, 7, 8])

print(c1)
print(c2)
print()

print("Combined")
print(c1 + c2)
print()

print("Subtraction")
print(c1 - c2)
print()

print("Intersection (positive minimums)")
print(c1 & c2)
print()

print("Union (maximums)")
print(c1 | c2)
