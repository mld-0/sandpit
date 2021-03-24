
def list_common_items(a, b):
    a_set = set(a)
    b_set = set(b)
    ab_set = a_set & b_set
    print(ab_set)

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]

list_common_items(color1, color2)
