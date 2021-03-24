
def listofstr_to_list(values):
    result = [c for L in values for c in L]
    print(result)

values = ['red', 'white', 'a', 'b', 'black', 'f']
listofstr_to_list(values)
