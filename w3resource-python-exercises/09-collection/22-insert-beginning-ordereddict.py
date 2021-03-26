from collections import OrderedDict

def insert_beginning_ordereddict(d, k, v):
    d.update({k:v})
    d.move_to_end(k, last=False)
    print(d)

d = OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
k = 'color4'
v = 'Orange'
insert_beginning_ordereddict(d, k, v)

