
def remove_elements_present_in_other(a, b):
    result = [x for x in a if x not in b]
    print(result)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8]

remove_elements_present_in_other(a, b)
