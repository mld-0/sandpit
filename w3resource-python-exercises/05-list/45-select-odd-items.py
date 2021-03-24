
def select_odd_items(values):
    result = [x for x in values if x % 2 != 0]
    print(result)

select_odd_items([1, 2, 3, 4, 5, 6, 7, 8, 9])
