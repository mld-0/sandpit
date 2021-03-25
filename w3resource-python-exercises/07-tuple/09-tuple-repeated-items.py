from collections import Counter

def tuple_repeated_items(values):
    result_counter = {k:v for k,v in Counter(values).items() if v > 1}
    print(result_counter)

t = (2, 4, 5, 6, 2, 3, 4, 4, 7)
tuple_repeated_items(t)

