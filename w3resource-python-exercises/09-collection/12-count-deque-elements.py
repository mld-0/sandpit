import collections

values = (2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,0)
values_set = set(values)

d = collections.deque(values)
print(d)

d_counts = {x: d.count(x) for x in values_set}
print(dict(sorted(d_counts.items(), key=lambda x: x[1], reverse=True)))

