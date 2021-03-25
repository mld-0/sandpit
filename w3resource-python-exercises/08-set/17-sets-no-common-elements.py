
def sets_no_common_elements(a, b):
    a_and_b = set(a) & set(b)
    print(len(a_and_b) == 0)

x = {1,2,3,4}
y = {4,5,6,7}
z = {8}

sets_no_common_elements(x, y)
sets_no_common_elements(x, z)
sets_no_common_elements(y, z)


