
def dict_total_str_len_values(d):
    result_len = {k: len(v) for k,v in d.items() if isinstance(v, str)}
    result_sum = sum(result_len.values())
    print(result_sum)

d = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
dict_total_str_len_values(d)
