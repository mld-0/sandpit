import heapq

#   Assuming matrix is sorted by row and column
def matrix_kth_smallest(values, k):
    pass
    values_flat = [x for L in values for x in L]
    result = heapq.nsmallest(k, values_flat)
    print(result[-1])

values = [ [0, 5, 9], [11, 12, 13], [15, 17, 19]   ]
matrix_kth_smallest(values, 1)
matrix_kth_smallest(values, 2)
matrix_kth_smallest(values, 3)
