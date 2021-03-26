import heapq

def heapsort_item_by_item(values):
    h = []
    for x in values:
        heapq.heappush(h, x)
    result = [heapq.heappop(h) for i in range(len(h))]
    print(result)

values = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapsort_item_by_item(values)

