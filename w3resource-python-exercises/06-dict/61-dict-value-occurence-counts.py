from collections import Counter

def dict_value_occurence_counts(d):
    result_counter = Counter(d.values())
    print(result_counter)

d = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
dict_value_occurence_counts(d)

