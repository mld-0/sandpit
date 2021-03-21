
def remove_unwanted(_str, unwanted):
    result = ""
    for c in _str:
        if not c in unwanted:
            result += c
    print(result)

unwanted = ["#", "*", "!", "^", "%"]
remove_unwanted("Pyth*^on Exercis^es", unwanted)
remove_unwanted("A%^!B#*CD", unwanted)
