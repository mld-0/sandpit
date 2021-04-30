import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)

values.head(10).plot(kind='bar', figsize=(20,8))
#plt.show()

