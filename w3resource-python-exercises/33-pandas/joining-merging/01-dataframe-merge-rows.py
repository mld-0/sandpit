import pandas as pd

student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})

print("student_data1:")
print(student_data1)
print("student_data2:")
print(student_data2)
print()

#   Note: pd.concat() preserves the origional index values of each input (resulting in duplicate index values), 
result_concat = pd.concat([student_data1, student_data2])
print("result_concat:")
print(result_concat)

#   whereas pd.merge() results in a new index for the resulting dataframe
result_merge = pd.merge(student_data1, student_data2, how='outer')
print("result_merge:")
print(result_merge)

