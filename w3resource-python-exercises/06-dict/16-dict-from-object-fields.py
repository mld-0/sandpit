
class dictObj(object):
     def __init__(self):
         self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'
     def do_nothing(self):
         pass

def dict_from_obj_fields(X):
    d = X.__dict__
    print(d)

test = dictObj()
dict_from_obj_fields(test)


