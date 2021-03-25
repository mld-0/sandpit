
def sort_dict_by_value(d):
    d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d_sorted)

d = {'Math':81, 'Physics':83, 'Chemistry':87}
sort_dict_by_value(d)
