from collections import Counter

def item_maximum_frequency(values):
    result_counter = Counter(values)
    print(result_counter.most_common(1))

values = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
item_maximum_frequency(values)
