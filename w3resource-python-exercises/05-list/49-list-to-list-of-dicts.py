
def list_to_list_of_dicts(values):
    #result = dict(zip(*values))
    result = [{'color': color, 'code': code} for color, code in zip(*values)]
    print(result)

values = [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]
list_to_list_of_dicts(values)
