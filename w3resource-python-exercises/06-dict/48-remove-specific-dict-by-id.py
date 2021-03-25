
def remove_specific_dict_by_key(values, _str):
    result = []
    for L in values:
        loop_dict = dict()
        if not _str in L.values():
            for k, v in L.items():
                loop_dict.update({k:v})
            result.append(loop_dict)
    #   or
    result = [{k: v for k, v in L.items()} for L in values if _str not in L.values()]
    print(result)

values = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
_str = '#FF0000'
remove_specific_dict_by_key(values, _str)
