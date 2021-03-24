
def rounded_elements_sum_multi_len(values):
    values_rounded = [round(x) for x in values]
    values_rounded_sum = sum(values_rounded)
    result = values_rounded_sum * len(values)
    print(result)

values = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5] 
rounded_elements_sum_multi_len(values)


