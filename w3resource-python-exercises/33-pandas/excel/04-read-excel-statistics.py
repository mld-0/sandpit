import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)
print()

print("Sum:", values["Production (short tons)"].sum()) 
print("Mean:", values["Production (short tons)"].mean())
print("Maximum:", values["Production (short tons)"].max())
print("Minimum:", values["Production (short tons)"].min()) 

