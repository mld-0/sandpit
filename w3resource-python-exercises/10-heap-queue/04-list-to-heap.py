import heapq

def list_to_heap(values):
    result = values[:]
    heapq.heapify(result)
    print(result)

values = [25, 44, 68, 21, 39, 23, 89]
list_to_heap(values)


