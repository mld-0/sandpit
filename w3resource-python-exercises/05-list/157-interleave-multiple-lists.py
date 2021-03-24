import itertools

def interleave_multiple_lists(*values):
    result = []
    for i, v in enumerate(itertools.zip_longest(*values)):
        for j, x in enumerate(v):
            if i < len(values[j]):
                result.append(x)
    print(result)

a=[2, 4, 7, 0, 5, 8]
b=[2, 5, 8]
c=[0, 1]
d=[3, 3, -1, 7]
    
interleave_multiple_lists(a, b, c, d)
