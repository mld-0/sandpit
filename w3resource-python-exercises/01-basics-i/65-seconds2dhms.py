import datetime

val_seconds = 1234565

delta = datetime.timedelta(seconds=val_seconds)
print(delta)

val_d = delta.days
val_s = delta.seconds
val_h = val_s // 3600
val_m = (val_s // 60) % 60

print("%s, %s, %s, %s" % (val_d, val_h, val_m, val_s))
