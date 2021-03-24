
def same_pair_three_lists(a, b, c):
    result = 0
    for i in range(len(a)):
        if a[i] == b[i] == c[i]:
            result += 1
    print(result)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [2, 2, 3, 1, 2, 6, 7, 9]
c = [2, 1, 3, 1, 2, 6, 7, 9]

same_pair_three_lists(a, b, c)
