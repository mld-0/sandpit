import collections.abc

num = [2,2,4,6,6,8,6,10,4]
print(num)

collect_num = collections.Counter(num)
print(collect_num)

collect_sum = sum(collect_num.values())
print(collect_sum)
