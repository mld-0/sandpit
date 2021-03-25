
def check_no_elements_in_set(a, b):
    result = sn1.isdisjoint(sn2)
    #   or
    result = len(sn1 & sn2) == 0
    print(result)

sn1 = {1,2,3}
sn2 = {4,5,6}
sn3 = {3}

check_no_elements_in_set(sn1, sn2)

