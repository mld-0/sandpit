import heapq

heap = [25, 44, 68, 21, 39, 23, 89]

heapq.heapify(heap)
result = heapq.heappop(heap)
value = 27
heapq.heappush(heap, value)
print(heap)

