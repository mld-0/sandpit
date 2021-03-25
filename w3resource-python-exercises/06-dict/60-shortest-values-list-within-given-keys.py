
def shortest_values_list_within_given_keys(d):
    d_values_len = {k: len(v) for k, v in d.items()}
    min_len = min(d_values_len.values())
    d_shortest_keys = [k for k,v in d_values_len.items() if v == min_len]
    print(d_shortest_keys)

d = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
shortest_values_list_within_given_keys(d)
