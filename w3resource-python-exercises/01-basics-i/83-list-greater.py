def list_greater(num, val):
    check = all(x <= val for x in num)
    print(check)

vals = [1, 4]
num = [2, 3, 4]

for val in vals:
    list_greater(num, val)
