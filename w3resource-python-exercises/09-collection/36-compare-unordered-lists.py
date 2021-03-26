from collections import Counter

def compare_unordered_lists(a, b):
    a_count = Counter(a)
    b_count = Counter(b)
    print(a_count == b_count)


n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]
compare_unordered_lists(n1, n2)
