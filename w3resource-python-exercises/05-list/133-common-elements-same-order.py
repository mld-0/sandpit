
def common_elements_same_order(a, b):
    ab_set = set(a) & set(b)
    ab_set_a = [x for x in a if x in ab_set]
    ab_set_b = [x for x in b if x in ab_set]
    print(ab_set_a == ab_set_b)

a = ['red', 'green', 'black', 'orange']
b = ['red', 'pink', 'green', 'white', 'black']
c = ['white', 'orange', 'pink', 'black']

common_elements_same_order(a, b)
common_elements_same_order(a, c)
common_elements_same_order(b, c)

