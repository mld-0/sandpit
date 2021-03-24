
def list_difference(a, b):
    a_set = set(a)
    b_set = set(b)

    a_not_b = a_set - b_set
    b_not_a = b_set - a_set

    ab_difference = a_not_b | b_not_a

    print(ab_difference)

list1 = [1, 3, 5, 7, 9]
list2 =[ 1, 2, 4, 6, 7, 8]
list_difference(list1, list2)
