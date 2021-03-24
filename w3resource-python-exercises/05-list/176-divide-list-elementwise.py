
def divide_list_elementwise(a, b):
    results = [a/b for a, b in zip(a, b)]
    print(results)

a = [7,2,3,4,9,2,3]
b = [9,8,2,3,3,1,2]
divide_list_elementwise(a, b)
