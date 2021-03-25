
def highest_n_kv(d, n):
    d_sorted = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    print(list(d_sorted)[0:n])
    
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
highest_n_kv(my_dict, 3)

