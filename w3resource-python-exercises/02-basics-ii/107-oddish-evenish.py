
def oddish_evenish(n):
    sum_digits = sum([int(x) for x in str(n)])
    if (sum_digits % 2 == 0):
        print("Evenish")
    else:
        print("Oddish")

oddish_evenish(120)
oddish_evenish(321)
oddish_evenish(43)
oddish_evenish(4433)
oddish_evenish(373)

