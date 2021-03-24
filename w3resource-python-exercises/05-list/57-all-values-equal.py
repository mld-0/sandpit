
def all_values_equal(values, item):
    result = all([x == item for x in values])
    print(result)

color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
item = 'green'

all_values_equal(color1, item)
all_values_equal(color2, item)
