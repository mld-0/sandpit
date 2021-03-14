values_str = input("Enter csv values:\n")

values = [int(x) for x in values_str.split(',')]
#   or
values = list(map(int, values_str.split(',')))

print(values)
