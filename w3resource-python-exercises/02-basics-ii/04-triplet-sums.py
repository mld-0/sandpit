def triplet_sums(values):
    result = []
    for i in range(len(values)):
        x = values[i]
        for j in range(i+1, len(values)):
            y = values[j]
            for k in range(j+1, len(values)):
                z = values[k]
                if (x + y + z == 0):
                    result.append([x, y, z])
    print(result)
                
values = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
triplet_sums(values)

#   or

import itertools
result = list(filter(lambda x: sum(x) == 0, list(itertools.permutations(values, 3))))  # contains 'duplicates' - same values in different orders
print(result)
