
def sum_elements_tuple_in_list(values):
    result_sum = [sum(x) for x in values]
    print(result_sum)

values = [(1, 2), (2, 3), (3, 4)]
sum_elements_tuple_in_list(values)

values = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
sum_elements_tuple_in_list(values)

