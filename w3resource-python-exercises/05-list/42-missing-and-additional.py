
def missing_and_additional(a, b):
    a_set = set(a)
    b_set = set(b)

    a_not_b = b_set - a_set
    b_not_a = a_set - b_set

    print(b_not_a)
    print(a_not_b)

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

missing_and_additional(list1, list2)
