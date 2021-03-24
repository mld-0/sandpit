import itertools

def digits_list_to_val(values):
    result = int(''.join([str(x) for x in values]))
    return result

def largest_int_digit_combination(values):
    values_combinations = itertools.permutations(values)
    values_int = map(digits_list_to_val, values_combinations)
    result = max(values_int)
    print(result)
     
values = [3, 40, 41, 43, 74, 9]
largest_int_digit_combination(values)

values = [10, 40, 20, 30, 50, 60]
largest_int_digit_combination(values)

values = [8, 4, 2, 9, 5, 6, 1, 0]
largest_int_digit_combination(values)

