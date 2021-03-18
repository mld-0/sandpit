
def remove_all_instances(values, n):
    result = values[:]
    while n in result:
        result.remove(n)
    print(len(result))

remove_all_instances([1, 2, 3, 4, 5, 6, 7, 5], 5)
remove_all_instances([10,10,10,10,10], 10)
remove_all_instances([10,10,10,10,10], 20)
remove_all_instances([], 1)
