
def dict_to_list_of_lists(d):
    result_list = [[k, v] for k, v in d.items()]
    #   or
    result_list = list(map(list, d.items()))
    print(result_list)

d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dict_to_list_of_lists(d)

d = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
dict_to_list_of_lists(d)
