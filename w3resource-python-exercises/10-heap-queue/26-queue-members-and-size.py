import queue

q = queue.Queue()
print(q.empty())

for x in range(4):
    q.put(x)

print(q.empty())

for n in list(q.queue):
    print(n, end=' ')
print()

print(q.qsize())
