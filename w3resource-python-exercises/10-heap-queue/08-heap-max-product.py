import heapq
import functools
import operator

values = [12, 74, 9, 50, 61, 41]
h = []

for x in values:
    heapq.heappush(h, x)

result_digits = heapq.nlargest(3, h)
result = functools.reduce(operator.mul, result_digits)

print(result_digits)
print(result)
