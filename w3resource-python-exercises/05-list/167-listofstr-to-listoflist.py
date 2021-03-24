
def listofstr_to_listoflists(values):
    result = [[c for c in L] for L in values]
    print(result)

values = ['Red', 'Maroon', 'Yellow', 'Olive']
listofstr_to_listoflists(values)
