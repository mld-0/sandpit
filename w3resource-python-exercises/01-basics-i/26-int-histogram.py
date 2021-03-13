
def int_histogram(values):
    hist_char = '*'
    for value in values:
        for i in range(value):
            print(hist_char, end='')
        print()

values = [2, 3, 6, 5]
int_histogram(values)
