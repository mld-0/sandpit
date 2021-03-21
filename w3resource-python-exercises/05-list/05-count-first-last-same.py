
def count_first_last_same(values):
    result_count = 0
    for x in values:
        if len(x) > 1 and x[0] == x[-1]:
            result_count += 1
    print(result_count)

count_first_last_same(['abc', 'xyz', 'aba', '1221'])
