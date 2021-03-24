
def insert_every_nth(values, n, item):
    result = []
    for i, x in enumerate(values):
        if i != 0 and i % n == 0:
            result.append(item)
        result.append(x)
    print(result)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
insert_every_nth(values, 2, 'a')
insert_every_nth(values, 4, 'b')
