import tempfile
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
print()

#   Read each sheet in spreadsheet as dataframe
_sheets_df = []
for loop_sheet in _sheets_employees:
    loop_df = pd.read_excel(_path_employees, sheet_name=loop_sheet)
    _sheets_df.append(loop_df)

#   Since each sheet has the same columns, combine vertically
values = pd.concat(_sheets_df)
print("values:")
print(values)
print()

_path_tempdir = tempfile.gettempdir()
print("_path_tempdir:")
print(_path_tempdir)

values.to_excel(os.path.join(_path_tempdir, 'employee-export-noindex.xlsx'), index=False)
values.to_excel(os.path.join(_path_tempdir, 'employee-export.xlsx'))

