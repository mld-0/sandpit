import pandas as pd

student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})

exam_data = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
        'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]})

print("student_data1:")
print(student_data1)
print("student_data2:")
print(student_data2)
print("exam_data:")
print(exam_data)
print()

print("Join first two said dataframes along rows:")
result_data = student_data1.append(student_data2)
#   or
result_data = pd.concat([student_data1, student_data2])
print(result_data)
print()

print("Now join the said result_data and df_exam_data along student_id:")
final_merged_data = pd.merge(result_data, exam_data, on='student_id')
print(final_merged_data)

