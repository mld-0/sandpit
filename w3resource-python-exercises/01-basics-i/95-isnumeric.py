def is_numeric(val):
    try:
        val_float = float(val)
        print(True)
    except Exception as e:
        print(False)

var_str = 'a123'
is_numeric(var_str)

var_str = '123'
is_numeric(var_str)

