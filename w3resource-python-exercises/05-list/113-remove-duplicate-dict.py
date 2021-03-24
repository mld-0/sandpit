
def remove_duplicate_dict(values):
    result = []
    for x in values:
        if x not in result:
            result.append(x)
    print(result)

values = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
remove_duplicate_dict(values)

