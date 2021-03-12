import datetime
date_a = datetime.datetime(2014, 7, 2)
date_b = datetime.datetime(2014, 7, 11)
delta_days = (date_b - date_a).days
print("%s days" % delta_days)
