import bisect

values = [1,2,4,5]

val = 2
i = bisect.bisect_left(values, val)
print(values)
print("val=(%i), i=(%i)" % (val, i))

val = 4
i = bisect.bisect_left(values, val)
print(values)
print("val=(%i), i=(%i)" % (val, i))

