import bisect

def bisect_first_occurence(values, item):
    if not item in values:
        index = -1
    else:
        index = bisect.bisect_left(values, item)
    print("item=(%i), index=(%i)" % (item, index))

    
values = [1, 2, 3, 4, 8, 8, 10, 12] 
print(values)

item = 8
bisect_first_occurence(values, item)

item = 1
bisect_first_occurence(values, item)

item = 2
bisect_first_occurence(values, item)

item = 9
bisect_first_occurence(values, item)


