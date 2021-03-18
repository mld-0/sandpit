
def isomorphic_strings(a, b):
    map_ab = dict()
    map_ba = dict()
    if (len(a) != len(b)):
        print(False)
        return
    for ca, cb in zip(a, b):
        if not ca in map_ab:
            map_ab[ca] = cb
        else:
            if not map_ab[ca] == cb:
                print(False)
                return 
        if not cb in map_ba:
            map_ba[cb] = ca
        else:
            if not map_ba[cb] == ca:
                print(False)
                return 
    print(True)
    return


isomorphic_strings("foo", "bar")
isomorphic_strings("bar", "foo")
isomorphic_strings("paper", "title")
isomorphic_strings("title", "paper")
isomorphic_strings("apple", "orange")
isomorphic_strings("aa", "ab")
isomorphic_strings("ab", "aa")
