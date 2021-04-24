import pandas as pd

student_data1  = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})


_list_of_dicts = [{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 203},
         {'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}]

_dict_of_lists = {k: [dic[k] for dic in _list_of_dicts] for k in _list_of_dicts[0]}

print("student_data1:")
print(student_data1)
print()

print("_list_of_dicts:")
print(_list_of_dicts)

print("_dict_of_lists:")
print(_dict_of_lists)

combined_data =  student_data1.append(_list_of_dicts, ignore_index=True)
print("combined_data (_list_of_dicts):")
print(combined_data)

combined_data = student_data1.append(pd.DataFrame(_dict_of_lists), ignore_index=True)
print("combined_data (_dict_of_lists):")
print(combined_data)

