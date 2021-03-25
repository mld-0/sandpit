
def str_to_num(_str):
    try:
        result = float(_str)
        return result
    except Exception:
        pass
    try:
        result = int(_str)
        return result
    except Exception:
        pass
    return None

def dict_values_str_to_num(values):
    result = [{k: str_to_num(v) for k, v in V.items()} for V in values]
    print(result)


values = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
dict_values_str_to_num(values)

values = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
dict_values_str_to_num(values)

