
def list_values_to_string(values):
    delim = ","
    values_str = [str(x) for x in values]
    result = delim.join(values_str)
    print(result)

list_values_to_string(['Red', 100, -50, 'green', 'w,3,r', 12.12, False])
