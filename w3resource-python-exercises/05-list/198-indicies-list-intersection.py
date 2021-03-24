
def indicies_list_intersection(a, b):
    ab_intersection = set(a) & set(b)
    #print(ab_intersection)
    a_intersection_indices = [i for i in range(len(a)) if a[i] in ab_intersection]
    print(a_intersection_indices)

a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 5, 2, 10, 12]
indicies_list_intersection(a, b)

a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 5, 7, 10, 12]
indicies_list_intersection(a, b)

a = [1, 2, 3, 4, 15, 6]
b = [7, 8, 5, 7, 10, 12]
indicies_list_intersection(a, b)
