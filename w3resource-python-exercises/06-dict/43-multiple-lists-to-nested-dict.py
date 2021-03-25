
def multiple_lists_to_nested_dict(a, b, c):
    result = []
    for i, j, k in zip(a, b, c):
        loop_dict = {i: {j: k}}
        result.append(loop_dict)
    #   or
    result = [{i: {j: k}} for i, j, k in zip(a, b, c)]
    print(result)
        

a = ['S001', 'S002', 'S003', 'S004']
b = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c = [85, 98, 89, 92]
multiple_lists_to_nested_dict(a, b, c)

