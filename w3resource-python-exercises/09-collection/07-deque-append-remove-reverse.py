import collections

deque_colors = collections.deque(["Red","Green","White"])

#   append to left
deque_colors.appendleft("Pink")
#   append to right
deque_colors.append("Orange")
print(deque_colors)

#   remove from left
deque_colors.popleft()
#   remove from right
deque_colors.pop()
print(deque_colors)

#   reverse
deque_colors.reverse()
print(deque_colors)

