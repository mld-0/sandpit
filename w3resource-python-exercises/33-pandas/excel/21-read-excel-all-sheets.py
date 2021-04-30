import os
import numpy as np
import pandas as pd

#   Spreadsheet file
_path_employees = 'employee.xlsx'

if not os.path.isfile(_path_employees):
    raise Exception("not found, _path_employees=(%s)" % _path_employees)

_xl = pd.ExcelFile(_path_employees)

#   Get names of each sheet in spreadsheet
_sheets_employees = _xl.sheet_names

print("_sheets_employees:")
print(_sheets_employees)

#   Read each sheet in spreadsheet as dataframe
_sheets_df = []
for loop_sheet in _sheets_employees:
    loop_df = pd.read_excel(_path_employees, sheet_name=loop_sheet)
    _sheets_df.append(loop_df)

#   Print each sheet
for loop_sheet, loop_df in zip(_sheets_employees, _sheets_df):
    print(loop_sheet)
    print(loop_df)

