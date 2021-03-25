
def remove_set_intersection(a, b):
    result = a.difference(b)
    #   or
    result = a - b
    print(result)

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}

remove_set_intersection(sn1, sn2)

