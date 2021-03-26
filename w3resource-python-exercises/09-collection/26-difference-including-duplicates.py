from collections import Counter

def difference_including_duplicates(a, b):
    a_counter = Counter(a)
    b_counter = Counter(b)

    a_not_b = a_counter - b_counter
    result = list(a_not_b.elements())
    print(result)

l1 = [1,1,2,3,3,4,4,5,6,7]
l2 = [1,1,2,4,5,6]
difference_including_duplicates(l1, l2)

