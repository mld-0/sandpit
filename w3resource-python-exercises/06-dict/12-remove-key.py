
def remove_key(d, k):
    d.pop(k)
    #   or
    #del d[k]
    print(d)

myDict = {'a':1,'b':2,'c':3,'d':4}
remove_key(myDict, 'a')
