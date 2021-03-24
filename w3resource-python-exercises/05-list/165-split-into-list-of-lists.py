import math

def split_into_list_of_lists(values, n):
    result = [[values[i+j*n] for i in range(n) if i+j*n < len(values)] for j in range(math.ceil(len(values)/n))]
    #   or
    result = [values[i:i+n] for i in range(0, len(values), n)]
    print(result)

values = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

split_into_list_of_lists(values, 3)
split_into_list_of_lists(values, 4)
split_into_list_of_lists(values, 5)

