import heapq

def heapq_merge(a, b):
    result = list(heapq.merge(a, b))
    print(result)

nums1 = [1, 3, 5, 7, 9, 11]
nums2 = [0, 2, 4, 6, 8, 10]
heapq_merge(nums1, nums2)
