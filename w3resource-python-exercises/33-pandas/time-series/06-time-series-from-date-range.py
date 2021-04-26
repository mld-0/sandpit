import pandas as pd
import numpy as np
import datetime

dates = ['2014-08-01','2014-08-02','2014-08-03','2014-08-04']

time_series = pd.Series(np.random.randint(1,10,4), dates)
print("time_series:")
print(time_series)

