
sort_mixed_list = lambda x: sorted(x, key=lambda a: (isinstance(a, str), a))

mixed_list = [19,'red',12,'green','blue', 10,'white','green',1]

print(mixed_list)
print(sort_mixed_list(mixed_list))

