
def insert_element_kth(values, n, k):
    result = values[:k] + [n] + values[k:]
    print(result)

values = [1, 1, 2, 3, 4, 4, 5, 1]
insert_element_kth(values, 12, 2)
