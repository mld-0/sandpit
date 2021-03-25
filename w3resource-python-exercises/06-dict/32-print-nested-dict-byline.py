
def print_nested_dict_byline(d):
    for k, v in d.items():
        print("%s:" % k)
        for a, b in v.items():
            print("%s: %s" % (a, b))

students = {'Aex':{'class':'V', 'rolld_id':2}, 'Puja':{'class':'V', 'roll_id':3}}
print_nested_dict_byline(students)
