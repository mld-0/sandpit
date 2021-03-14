def max_and_min(values):
    _max = None
    _min = None
    for val in values:
        if (_max is None) or (val > _max):
            _max = val
        if (_min is None) or (val < _min):
            _min = val
    print(f"max=({_max})")
    print(f"min=({_min})")

values = [0, 10, 15, 40, -5, 42, 17, 28, 75]
max_and_min(values)
