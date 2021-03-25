
def dict_top_three_values(d):
    d_sorted = list(sorted(d.items(), key=lambda x: x[1], reverse=True))
    for k, v in d_sorted[:3]:
        print(k, v)

d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
dict_top_three_values(d)

