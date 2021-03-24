
def add_to_elements(values, item):
    result = [x+item for x in values]
    print(result)

values = [3, 8, 9, 4, 5, 0, 5, 0, 3]
add_to_elements(values, 3)

values = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
add_to_elements(values, 0.51)
