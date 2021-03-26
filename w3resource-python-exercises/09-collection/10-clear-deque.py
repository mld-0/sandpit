import collections

odd_nums = (1,3,5,7,9)
odd_deque  = collections.deque(odd_nums)
print(odd_deque)

odd_deque.clear()
print(odd_deque)

