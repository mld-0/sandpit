
def pairs_to_sorted_unique(L):
    L_unique = set().union(*L)
    L_unique_sorted = sorted(L_unique)
    print(L_unique_sorted)

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
pairs_to_sorted_unique(L)

