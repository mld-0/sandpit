#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import numpy as np
#   {{{2

def mergesort_singular(values):
    """Implement mergesort in a single python function, sorts input array 'values' in-place"""
    #   A list of length 1 is by definition sorted
    if len(values) == 1:
        return 
    #   Divide list into two halves (and make a copy of each)
    mid = len(values)//2
    L = values[:mid]
    R = values[mid:]
    #   Sort the first and second halves
    mergesort_singular(L)
    #print("values=(%s)" % str(values))
    print("L=(%s)" % str(L))
    mergesort_singular(R)
    #print("values=(%s)" % str(values))
    print("R=(%s)" % str(R))
    #   Combine L, R to create sorted result in array values
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            values[k] = L[i]
            i += 1
        else:
            values[k] = R[j]
            j += 1
        k += 1
    #   Add remaining values 
    while i < len(L):
        values[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        values[k] = R[j]
        j += 1
        k += 1
    print("values=(%s)" % str(values))

#   {{{
def mergesort_caller(values):
    """Implement mergesort with aid of function mergesort_merge, sorts input array 'values' in-place"""
    #   A list of length 1 is by definition sorted
    if len(values) == 1:
        return 
    #   Divide list into two halves
    mid = len(values)//2
    L = values[:mid]
    R = values[mid:]
    #   Sort the first and second halves
    mergesort_caller(L)
    mergesort_caller(R)
    #   Combine L, R to create sorted result in array values
    mergesort_merge(values, L, R)

def mergesort_merge(values, L, R):
    """Assuming L, R are sorted arrays, merge values into sorted array result and return"""
    i = j = k = 0
    #   Combine L, R to create sorted result in array values
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            values[k] = L[i]
            i += 1
        else:
            values[k] = R[j]
            j += 1
        k += 1
    #   Add remaining values 
    while i < len(L):
        values[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        values[k] = R[j]
        j += 1
        k += 1

def mergesort_returned(values):
    """Implement mergesort, without modifying input array values"""
    #   A list of length 1 is by definition sorted
    if len(values) == 1:
        return values
    #   Divide list into two halves
    mid = len(values)//2
    L = values[:mid]
    R = values[mid:]
    #   Sort the first and second halves
    L = mergesort_returned(L)
    R = mergesort_returned(R)
    #   Combine L, R to create sorted result in array values
    #result = mergesort_merge(L, R)
    result = [0] * len(values)
    i = j = k = 0
    #   Combine L, R to create sorted result in array result
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result[k] = L[i]
            i += 1
        else:
            result[k] = R[j]
            j += 1
        k += 1
    #   Add remaining values 
    while i < len(L):
        result[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        result[k] = R[j]
        j += 1
        k += 1
    return result
#   }}}

if __name__ == '__main__':
    values = [12, 11, 13, 5, 6, 7]
    values = list(np.random.randint(1, 1000, 100))
    print("values:")
    print(values)
    mergesort_singular(values)
    print("values:")
    print(values)
    print()

    #   {{{
    #values = [12, 11, 13, 5, 6, 7]
    #values = list(np.random.randint(1, 1000, 100))
    #print("values:")
    #print(values)
    #mergesort_caller(values)
    #print("values:")
    #print(values)
    #print()

    #values = [12, 11, 13, 5, 6, 7]
    #values = list(np.random.randint(1, 1000, 100))
    #print("values:")
    #print(values)
    #result = mergesort_returned(values)
    #print("result:")
    #print(result)
    #   }}}


#   }}}1

