
def multi_list_common_elements(a, b, c):
    results = []
    for i in range(min(len(a), len(b), len(c))):
        if a[i] == b[i] and b[i] == c[i]:
            results.append(a[i])
    print(results)

a = [1, 1, 3, 4, 5, 6, 7]
b = [0, 1, 2, 3, 4, 5, 7]
c = [0, 1, 2, 3, 4, 5, 7]

multi_list_common_elements(a, b, c)
        
