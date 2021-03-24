from collections import Counter

def count_elements_in_range(values, a, b):
    values_filtered = [x for x in values if x >= a and x < b]
    values_filtered_count = Counter(values_filtered)
    print(values_filtered_count)

list1 = [10,20,30,40,40,40,70,80,99]
count_elements_in_range(list1, 40, 100)

