def near_center(n):
    if (abs(1000 - n) <= 100):
        print(True)
    elif (abs(2000 - n) <= 100):
        print(True)
    else:
        print(False)


vals = [1000,900,800,2200]

for n in vals:
    result = near_center(n)
