import collections

t = (2, 4, 6)

d = collections.deque(t)

d.append(8)
d.append(10)
d.append(12)
d.appendleft(2)
print(type(d))
print(d)
