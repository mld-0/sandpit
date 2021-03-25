
def sort_dict_by_key(d):
    d_sorted = sorted(d.items(), key=lambda x: x[0])
    print(d_sorted)

color_dict = {'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'#FFFFFF'}
sort_dict_by_key(color_dict)

