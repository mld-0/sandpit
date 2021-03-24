
def element_difference(values):
    result = [values[i+1] - values[i] for i in range(len(values)-1)]
    print(result)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element_difference(values)

values = [2, 4, 6, 8]
element_difference(values)

