
def index_item_in_tuple(t, item):
    result_index = [i for i in range(len(t)) if t[i] == item]
    print(result_index)


t = tuple("index tuple")
index_item_in_tuple(t, 'p')
print(t.index('p'))

#create a tuple
tuplex = tuple("index tuple")
print(tuplex)
#get index of the first item whose value is passed as parameter
index = tuplex.index("p")
print(index)
#define the index from which you want to search
index = tuplex.index("p", 5)
print(index)
#define the segment of the tuple to be searched
index = tuplex.index("e", 3, 6)
print(index)
#if item not exists in the tuple return ValueError Exception
#index = tuplex.index("y")
