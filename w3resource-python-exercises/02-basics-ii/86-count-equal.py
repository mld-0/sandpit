
def count_equal(values):
    duplicates = set()
    for i in range(len(values)-1):
        for j in range(i, len(values)):
            if values[i] == values[j] and i != j:
                duplicates.add(values[i])
    count = 0
    for d in duplicates:
        count += values.count(d)
    print(count)
        
count_equal((1, 1, 1))
count_equal((1, 2, 2))
count_equal((-1, -2, -3))
count_equal((-1, -1, -1))
