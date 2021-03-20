
def check_evenodd(values):
    """Check even indexs contain even values, and odd indexes contain odd values for list values."""
    result = True
    for i, v in enumerate(values):
        if not (i % 2 == v % 2):
            result = False
    print(result)

check_evenodd([2, 1, 4, 3, 6, 7, 6, 3])
check_evenodd([2, 1, 4, 3, 6, 7, 6, 4])
check_evenodd([4, 1, 2])

