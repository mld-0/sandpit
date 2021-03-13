
def compound_intrest(amount, intrest, years):
    result = amount * (1 + intrest / 100) ** years
    print(result)

amount = 10000
intrest = 3.5
years = 7
compound_intrest(amount, intrest, years)
