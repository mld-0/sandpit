
def replace_last_list_of_tuples(values, item):
    result = []
    for x in values:
        x = list(x)
        x[-1] = item
        result.append(tuple(x))
    print(result)

values = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
replace_last_list_of_tuples(values, 100)
