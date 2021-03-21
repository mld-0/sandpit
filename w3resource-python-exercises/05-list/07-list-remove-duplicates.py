
def list_remove_duplicates(values):
    result_list = []
    for n in values:
        if not n in result_list:
            result_list.append(n)
    print(result_list)

list_remove_duplicates([10,20,30,20,10,50,60,40,80,50,40])


