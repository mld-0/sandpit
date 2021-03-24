
def nth_element_exists(values, n):
    result = None
    try:
        result = values[n]
        result = True
    except Exception as e:
        result = False
    print(result)

x = [1, 2, 3, 4, 5, 6]
nth_element_exists(x, 2)
nth_element_exists(x, 12)
