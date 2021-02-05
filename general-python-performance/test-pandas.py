
import numpy as np
import pandas as pd
from datetime import datetime

time_start = datetime.now()

df = pd.DataFrame()
df['X'] = np.random.randint(low=100, high=999, size=100000000)
df['X_squared'] = df['X'].apply(lambda x: x**2)
df['X_sqrt'] = df['X'].apply(lambda x: x**0.5)
df['Mul'] = df['X_squared'] * df['X_sqrt']
df['Div'] = df['X_squared'] / df['X_sqrt']
df['Int_div'] = df['X_squared'] // df['X_sqrt']

time_end = datetime.now()
print(f'Total time = {(time_end - time_start).seconds} seconds')
