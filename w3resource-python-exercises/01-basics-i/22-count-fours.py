
def count_fours(vals):
    count = 0
    for val in vals:
        if (val == 4):
            count += 1
    print(count)

vals = [1, 4, 6, 7, 4]
count_fours(vals)
vals = [1, 4, 6, 4, 7, 4]
count_fours(vals)

