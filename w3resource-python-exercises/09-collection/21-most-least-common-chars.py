from collections import Counter

def most_least_common_char(_str):
    result_counter = Counter(_str)
    result_counter_sorted = sorted(result_counter.items(), key=lambda x: x[1], reverse=True)
    result_most = result_counter_sorted[0][0]
    result_least = result_counter_sorted[-1][0]
    print(result_most)
    print(result_least)

_str = 'hello world'
most_least_common_char(_str)


