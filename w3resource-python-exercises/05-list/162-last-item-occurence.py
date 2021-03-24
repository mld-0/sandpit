
def last_item_occurence(values, item):
    loc_item = [i for i in range(len(values)) if values[i] == item]
    print(loc_item[-1])

values = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

last_item_occurence(values, 'f')
last_item_occurence(values, 'c')
last_item_occurence(values, 'k')
last_item_occurence(values, 'w')
