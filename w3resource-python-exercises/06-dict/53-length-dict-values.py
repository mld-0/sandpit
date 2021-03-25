
def length_dict_values(d):
    result = {v: len(v) for k,v in d.items()}
    print(result)

d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
length_dict_values(d)

d = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
length_dict_values(d)
