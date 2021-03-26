import collections

tup1 = (1,3,5,7,9)
dq1 = collections.deque(tup1)
dq2 = dq1.copy()
print(dq1)
print(id(dq1))

print(dq2)
print(id(dq2))

print(id(dq1[0]))
print(id(dq2[0]))
