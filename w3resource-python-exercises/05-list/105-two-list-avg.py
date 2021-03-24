
def two_list_avg(a, b):
    values = a + b
    result = sum(values) / len(values)
    print(result)

a = [1, 1, 3, 4, 4, 5, 6, 7]
b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
two_list_avg(a, b)
