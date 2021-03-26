import heapq

def heapqueue_three_largest(values):
    result_largest = heapq.nlargest(3, values)
    print(result_largest)

nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
heapqueue_three_largest(nums_list)
