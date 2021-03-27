import bisect

def bisect_last_occurence(values, item):
    if not item in values:
        index = -1
    else:
        index = bisect.bisect_right(values, item) - 1
    print("item=(%i), index=(%i)" % (item, index))

    
values = [1, 2, 3, 4, 8, 8, 10, 12] 
print(values)

item = 8
bisect_last_occurence(values, item)

item = 1
bisect_last_occurence(values, item)

item = 2
bisect_last_occurence(values, item)

item = 9
bisect_last_occurence(values, item)


