import tzlocal
import pandas as pd

print("Timezone: Europe/Berlin:")
date_pytz = pd.Timestamp('2019-01-01', tz='Europe/Berlin')
print(type(date_pytz.tz))
print(date_pytz.tz)  
print()

print("dateutil Berlin:")
date_util = pd.Timestamp('2019-01-01', tz='dateutil/Europe/Berlin')
print(type(date_util.tz))
print(date_util.tz)
print()

print("US/Pacific:")
date_pytz = pd.Timestamp('2019-01-01', tz='US/Pacific')
print(type(date_pytz.tz))
print(date_pytz.tz)  
print()

print("dateutil US Pacific:")
date_util = pd.Timestamp('2019-01-01', tz='dateutil/US/Pacific')
print(type(date_util.tz))
print(date_util.tz)
print()

print("tzlocal.get_localzone:")
date_local = pd.Timestamp('2019-01-01', tz=tzlocal.get_localzone())
print(type(date_local.tz))
print(date_local.tz)

