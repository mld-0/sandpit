import operator

def sort_dict(d):
    d_asc = dict(sorted(d.items(), key=lambda x: x[1]))
    #   or
    d_asc = dict(sorted(d.items(), key=operator.itemgetter(1)))
    print(d_asc)
    d_des = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    print(d_des)

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sort_dict(d)

