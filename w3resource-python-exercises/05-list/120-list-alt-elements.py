
def list_alt_elements(values):
    result = [x for x in values[::2]]
    print(result)


values = ['red', 'black', 'white', 'green', 'orange']
list_alt_elements(values)

values = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
list_alt_elements(values)

