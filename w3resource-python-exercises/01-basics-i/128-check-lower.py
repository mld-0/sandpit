def contains_upper(str1):
    str2 = str1.upper()
    if not str1 == str2:
        print("Lower case values")
    else:
        print("No lower case values")
    #   or
    #   if any(x.islower() for x in str1):

str1 = 'A8238i823acdeOUEI'
contains_upper(str1)

str1 = 'A8238I823ACDEOUEI'
contains_upper(str1)

