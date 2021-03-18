
def maximum_stock_profit(values):
    if len(values) == 0:
        print(0)
        return
    values_sorted = sorted(values, reverse=True)
    delta = values_sorted[0] - values_sorted[-1]
    print(delta)

maximum_stock_profit([8, 10, 7, 5, 7, 15])
maximum_stock_profit([1, 2, 8, 1])
maximum_stock_profit([])
