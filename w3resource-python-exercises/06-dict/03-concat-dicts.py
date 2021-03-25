
def concat_dicts(a, b, c):
    result = dict()
    result.update(a)
    result.update(b)
    result.update(c)
    print(result)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

concat_dicts(dic1, dic2, dic3)

