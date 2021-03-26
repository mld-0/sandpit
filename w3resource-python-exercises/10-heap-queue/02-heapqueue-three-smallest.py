import heapq

def heapqueue_three_smallest(values):
    result_largest = heapq.nsmallest(3, values)
    print(result_largest)

nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
heapqueue_three_smallest(nums_list)
