
def occurences_index(values, n):
    n_indexs = [i for i in range(len(values)) if values[i] == n]
    print(n_indexs)

occurences_index([1,2,3,4,5,2], 2)
occurences_index([3,1,2,3,4,5,6,3,3], 3)
occurences_index([1,2,3,-4,5,2,-4], -4)
