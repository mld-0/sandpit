
def list_difference(a, b):
    a_set = set(a)
    b_set = set(b)
    a_not_b = a_set - b_set
    b_not_a = b_set - a_set
    print(a_not_b)
    print(b_not_a)

a, b = ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
list_difference(a, b)

    
