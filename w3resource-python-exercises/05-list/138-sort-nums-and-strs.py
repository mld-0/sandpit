
def sort_nums_and_strs(values):
    values_num = [x for x in values if isinstance(x, int) or isinstance(x, float)]
    values_str = [x for x in values if isinstance(x, str)]
    values_num = sorted(values_num)
    values_str = sorted(values_str)
    result = values_num + values_str
    print(result)

values = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
sort_nums_and_strs(values)
