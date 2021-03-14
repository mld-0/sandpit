values = [25, '25', [25]]

for val in values:
    print(val)
    if isinstance(val, int):
        print("int")
    elif isinstance(val, str):
        print("str")
    else:
        print("other")
