
def is_valid_str(_str):
    uppers = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    lowers = [chr(x) for x in range(ord('a'), ord('z')+1)]
    min_length = 4
    if len(_str) < min_length:
        print(False)
        return
    contains_upper = _str != _str.lower()
    contains_lower = _str != _str.upper()
    if not (contains_upper and contains_lower):
        print(False)
        return
    print(True)
        
is_valid_str("W3resource")

