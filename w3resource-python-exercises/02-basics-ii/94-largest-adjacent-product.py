
def largest_adjacent_product(values):
    result = 0
    for loop_i in range(len(values)-1):
        for loop_j in range(loop_i+1, len(values)):
            result = max(values[loop_i] * values[loop_j], result)
    print(result)

largest_adjacent_product([1,2,3,4,5,6])
largest_adjacent_product([1,2,3,4,5])
largest_adjacent_product([2,3])
