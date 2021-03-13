val_int = 5245

val_str = str(val_int)

result = 0
for c in val_str:
    result += int(c)

print(result)
