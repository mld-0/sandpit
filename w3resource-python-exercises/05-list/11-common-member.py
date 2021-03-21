
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    ab_set = a_set & b_set
    print(len(ab_set) != 0)

    #   or

    result = False
    for loop_a in a:
        for loop_b in b:
            if loop_a == loop_b:
                result = True
    #print(result)

common_member([1,2,3,4,5], [5,6,7,8,9])
common_member([1,2,3,4,5], [6,7,8,9])
