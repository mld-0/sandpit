
def elements_in_nested_lists(a, b):
    results = [[x for x in bb if x in a] for bb in b]
    print(results)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
b = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

elements_in_nested_lists(a, b)

