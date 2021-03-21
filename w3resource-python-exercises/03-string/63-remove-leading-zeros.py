import re

def remove_ip_leading_zeros(_str):
    result = re.sub(r'\b0*([0-9]+?)\b', r'\1', _str)
    print(result)

remove_ip_leading_zeros("255.024.01.01")
remove_ip_leading_zeros("127.0.0.01 ")

