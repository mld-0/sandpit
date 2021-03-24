
def count_consecutive_duplicates(values):
    consecutive_items = []
    consecutive_count = []
    for i in range(len(values)-1):
        x = values[i]
        y = values[i+1]
        if x == y:
            if len(consecutive_items) != 0 and consecutive_items[-1] == x:
                consecutive_count[-1] += 1
            else:
                consecutive_items.append(x)
                consecutive_count.append(2)
    result = (consecutive_items, consecutive_count)
    print(result)


values = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
count_consecutive_duplicates(values)

