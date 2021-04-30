import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
values = values.sort_values(['Production (short tons)'], ascending=False)
print("values:")
print(values)

values['Production (short tons)'].head(10).plot(kind='barh')
#plt.show()

