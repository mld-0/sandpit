
def highest_sum_of_elements(values):
    result = sorted(values, key=lambda x: sum(x))[-1]
    #   or
    result = max(values, key=lambda x: sum(x))
    print(result)

values = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
highest_sum_of_elements(values)
