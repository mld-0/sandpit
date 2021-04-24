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

#   Results in duplicate column names
result = pd.concat([student_data1, student_data2], axis=1)
print("result concat:")
print(result)
print("result['student_id']:")
print(result['student_id'])
print()

#   Apply suffixes to column names to distinguish them in resulting dataframe
result = pd.concat([student_data1.add_suffix('_L'), student_data2.add_suffix('_R')], axis=1)
print("result concat (with suffixes):")
print(result)
print()

result = pd.merge(student_data1, student_data2, how='outer')
print("result merge:")
print(result)
