
def increasing_trend(values):
    """Determine whether a list of numbers is in increasing order."""
    values_sorted = sorted(values)
    if (values != values_sorted):
        print(False)
    else:
        print(True)

increasing_trend([1,2,3,4])
increasing_trend([1,2,5,3,4])
increasing_trend([-1,-2,-3,-4])
increasing_trend([-4,-3,-2,-1])
increasing_trend([1,2,3,4,0])
