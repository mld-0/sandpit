import datetime
import numpy as np

dt_start = datetime.datetime(2000, 1, 1)
print(dt_start)

dt_range = np.array([dt_start + datetime.timedelta(hours=i) for i in range(24)])
print(dt_range)

