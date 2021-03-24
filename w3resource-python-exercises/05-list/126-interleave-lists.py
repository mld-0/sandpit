
def interleave_lists(*values):
    result = []
    for V in zip(*values):
        for v in V:
            result.append(v)
    #   or
    result = [x for V in zip(*values) for x in V]
    print(result)

a = [1, 2, 3, 4, 5, 6, 7]
b = [10, 20, 30, 40, 50, 60, 70]
c = [100, 200, 300, 400, 500, 600, 700]

interleave_lists(a, b, c)

