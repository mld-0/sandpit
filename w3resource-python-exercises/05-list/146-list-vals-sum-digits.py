
def list_vals_sum_digits(values):
    result = sum([int(i) for x in values if isinstance(x, int) for i in str(abs(int(x)))])
    print(result)

values = [10, 2, 56]
list_vals_sum_digits(values)

values = [10, 20, 4, 5, 'b', 70, 'a']
list_vals_sum_digits(values)

values = [10, 20, -4, 5, -70]
list_vals_sum_digits(values)

