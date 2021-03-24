from collections import Counter

def item_maximum_occurences(values):
    results_counter = Counter(values)
    results = sorted(results_counter.items(), key=lambda x: x[1], reverse=True)
    result = results[0][0]
    print(result)

values = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
item_maximum_occurences(values)

