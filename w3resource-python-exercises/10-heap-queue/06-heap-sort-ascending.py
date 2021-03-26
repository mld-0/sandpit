import heapq

nums_list = [18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1]
heap = nums_list[:]

heapq.heapify(heap)

result = [heapq.heappop(heap) for i in range(len(heap))]
print(result)



