
def middle_chars(_str):
    if len(_str) % 2 == 0:
        print(_str[len(_str)//2-1:len(_str)//2+1])
    else:
        print(_str[len(_str)//2])

middle_chars("Python")
middle_chars("PHP")
middle_chars("Java")
