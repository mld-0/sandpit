
def remove_item_list_of_lists(values, n):
    result = [[x[i] for i in range(len(x)) if i+1 != n] for x in values]
    print(result)

values = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
remove_item_list_of_lists(values, 1)
remove_item_list_of_lists(values, 2)
remove_item_list_of_lists(values, 4)

