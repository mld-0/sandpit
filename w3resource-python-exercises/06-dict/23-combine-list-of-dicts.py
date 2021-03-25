
def combine_list_of_dicts(values):
    result = dict()
    for L in values:
        k, v = L['item'], L['amount']
        if k in result:
            result[k] += v
        else:
            result[k] = v
    print(result)

values = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
combine_list_of_dicts(values)

