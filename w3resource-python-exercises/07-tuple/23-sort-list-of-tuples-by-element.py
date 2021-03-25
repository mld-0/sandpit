
def sort_list_of_tuples_by_element(t):
    result = sorted(t, key=lambda x: x[1], reverse=True)
    print(result)

t = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sort_list_of_tuples_by_element(t)

