
def split_given_first_length(values, n):
    result = [values[:n]] + [values[n:]]
    print(result)

values = [1, 1, 2, 3, 4, 4, 5, 1]
split_given_first_length(values, 3)
