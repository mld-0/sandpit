
def check_contains_subset(values, subset):
    values_iter = values[:]
    for x in subset:
        if not x in values_iter:
            print(False)
            return
        values_iter.remove(x)
    print(True)
    

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
d = [3,7,7]

check_contains_subset(a, b)
check_contains_subset(a, c)
check_contains_subset(a, d)

