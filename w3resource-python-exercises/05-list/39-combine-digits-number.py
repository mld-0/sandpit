
def combine_digits_number(values):
    result_str = ''.join([str(x) for x in values])
    result = int(result_str)
    print(result)

combine_digits_number([11, 33, 50])

