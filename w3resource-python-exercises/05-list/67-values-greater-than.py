
def values_greater_than(values, n):
    result = [x for x in values if x > n]
    print(result)

list1 = [220, 330, 500]
list2 = [12, 17, 21]

values_greater_than(list1, 200)
values_greater_than(list2, 25)

