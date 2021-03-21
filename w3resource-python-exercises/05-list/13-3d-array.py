import pprint

def array_3d(a, b, c):
    fill = '*'
    result = []
    for i in range(a):
        list_j = []
        for j in range(b):
            list_k = []
            for k in range(c):
                list_k.append(fill)
            list_j.append(list_k)
        result.append(list_j)
    #   or
    result = [[[fill for k in range(c)] for j in range(b)] for i in range(a)]
    pprint.pprint(result)

array_3d(3, 4, 6)
