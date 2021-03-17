import math

def debt_calc(months):
    principle = 100_000
    total = principle
    rate = 0.05
    for i in range(months):
        total = int(math.ceil((total * (1 + rate)) / 1000)) * 1000
    print(total)

debt_calc(7)
