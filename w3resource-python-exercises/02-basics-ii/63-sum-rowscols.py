
def print_values(values):
    for row in values:
        for val in row:
            print("%i " % val, end='')
        print()

def sum_rowscols(values):
    results = []
    for i in range(len(values)):
        loop_result = []
        _sum = 0
        for j in range(len(values[0])):
            _sum += values[i][j]
            loop_result.append(values[i][j])
        loop_result.append(_sum)
        results.append(loop_result)

    loop_result = []
    for j in range(len(results[0])):
        _sum = 0
        for i in range(len(results)):
            _sum += results[i][j]
        loop_result.append(_sum)
    results.append(loop_result)
    return results

values = [[25, 69, 51, 26], [68, 35, 29, 54], [54, 57, 45, 63], [61, 68, 47, 59]]
results = sum_rowscols(values)
print_values(results)

