import datetime
import pandas as pd

start_date = datetime.date(2020,8,1)
end_date = datetime.date(2021,1,1)

date_range = pd.date_range(start_date, end_date)
date_range = date_range[date_range.day==1]

print(date_range)

from dateutil.relativedelta import relativedelta
import datetime

result = [(start_date + relativedelta(months=+m)).isoformat() for m in range(0,relativedelta(start_date,end_date).months+1)]
print(result)

