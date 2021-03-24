
def remove_kth_element(values, k):
    result = values[:k] + values[k+1:]
    print(result)

values = [1, 1, 2, 3, 4, 4, 5, 1]
remove_kth_element(values, 2)

