
def rounded_max_min_multi5(values):
    values = [round(x) for x in values]
    values_min = min(values)
    values_max = max(values)
    values = sorted([5*x for x in values])
    print(values)


values = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
rounded_max_min_multi5(values)

