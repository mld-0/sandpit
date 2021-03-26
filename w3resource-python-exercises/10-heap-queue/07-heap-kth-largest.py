import heapq

def heap_k_largest(values, k):
    h = []
    for x in values:
        heapq.heappush(h, -1 * x)  # multiply by -1 during push/pop for maxheap behaviour
    for i in range(k):
        w  = -1 * heapq.heappop(h)
    print(w)

values = [12, 14, 9, 50, 61, 41]
heap_k_largest(values, 3)
heap_k_largest(values, 2)
heap_k_largest(values, 5)



