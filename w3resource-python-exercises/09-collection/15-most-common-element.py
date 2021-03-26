from collections import Counter

def most_common_element(values):
    values_counter = Counter(values)
    print(values_counter)
    print(values_counter.most_common(1)[0][0])

values = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
most_common_element(values)

