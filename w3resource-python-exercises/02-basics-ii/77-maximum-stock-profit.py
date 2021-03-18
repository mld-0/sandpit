
def maximum_stock_profit(values):
    profit = 0
    buy = None
    sell = None
    for i in range(len(values)-1):
        for j in range(i, len(values)):
            loop_profit = values[j] - values[i]
            if (loop_profit > profit):
                profit = loop_profit
                buy = values[i]
                sell = values[j]
    print(profit)

maximum_stock_profit([224, 236, 247, 258, 259, 225])

