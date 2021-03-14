int_val = 30
print(int_val.bit_length())

if (int_val.bit_length() <= 63):
    print("Fits in 64bits")
