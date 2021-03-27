import bisect

def bisect_before_first_occurence(values, item):
    index = bisect.bisect_left(values, item) - 1
    print("item=(%i), index=(%i)" % (item, index))

    
values = [1, 2, 3, 4, 8, 8, 10, 12] 
print(values)

item = 5
bisect_before_first_occurence(values, item)

item = 1
bisect_before_first_occurence(values, item)

item = 2
bisect_before_first_occurence(values, item)

item = 9
bisect_before_first_occurence(values, item)


