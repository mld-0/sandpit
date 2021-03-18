
def employee_code_valid(code):
    if code.isnumeric() and (len(code) == 8 or len(code) == 12):
        print(True)
    else:
        print(False)
    
employee_code_valid('12345678')
employee_code_valid('1234567j')
employee_code_valid('12345678j')
employee_code_valid('123456789123')
employee_code_valid('123456abcdef')

