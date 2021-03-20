
def find_not_poor(_str):
    loc_not = _str.find('not')
    loc_poor = _str.find('poor')
    if loc_not < 0 or loc_poor < 0:
        print(_str)
        return
    result = _str[0:loc_not] + 'good' + _str[loc_poor+4:]
    print(result)

find_not_poor('The lyrics is not that poor!')
find_not_poor('The lyrics is poor!')
