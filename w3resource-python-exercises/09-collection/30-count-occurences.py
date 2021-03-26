from collections import Counter

def count_occurences(values):
    result_counter = Counter(values)
    print(result_counter)

values = ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
count_occurences(values)

values = [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
count_occurences(values)


