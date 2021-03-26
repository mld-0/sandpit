import heapq

def merge_multiple_sorted_inputs(*values):
    result_iter = heapq.merge(*values)
    result = list(result_iter)
    print(result)

num1 = sorted([25, 24, 15, 4, 5, 29, 110])
num2 = sorted([19, 20, 11, 56, 25, 233, 154])
num3 = sorted([24, 26, 54, 48])
merge_multiple_sorted_inputs(num1, num2, num3)

