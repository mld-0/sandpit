import pandas as pd

student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})


s6 = pd.Series(['S6', 'Scarlette Fisher', 205], index=['student_id', 'name', 'marks'])
#   or
s6 = pd.Series(['S6', 'Scarlette Fisher', 205], index=student_data1.columns)

print("student_data1:")
print(student_data1)
print()

print("New Row(s)")
print(s6)
print()

combined_data = student_data1.append(s6, ignore_index=True)
print("Combined Data:")
print(combined_data)

