import collections

d = collections.deque()
d.append(2)
d.append(4)
d.append(6)
d.append(8)
d.append(10)

print(d)
d.rotate()
print(d)
d.rotate(2)
print(d)

