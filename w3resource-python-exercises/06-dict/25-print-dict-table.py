
def print_dict_table(d):
    for k, v in d.items():
        print("%4s" % k, end='')
    print()
    for k, v in d.items():
        for x in v:
            print("%4s" % x, end='')
        print()
        

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print_dict_table(my_dict)
