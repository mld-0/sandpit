
def nth_order_derivative(n):
    if (n == 1):
        print("Linear")
    elif (n == 2):
        print("Quadratic")
    elif (n == 3):
        print("Cubic")
    else:
        print("%i order" % n)

def d_dt(values):
    return [values[x] - values[x-1] for x in range(1, len(values))]

def is_constant(values):
    values_set = set(values)
    return len(values_set) == 1

def linear_quadratic_cubic(values):
    count = 0
    while not is_constant(values):
        values = d_dt(values)
        count += 1
    nth_order_derivative(count)

linear_quadratic_cubic([0,2,4,6,8,10])
linear_quadratic_cubic([1,4,9,16,25])
linear_quadratic_cubic([0,12,10,0,-12,-20])
linear_quadratic_cubic([1,2,3,4,5])

