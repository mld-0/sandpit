
def int_representations(n):
    n_decimal = str(n)
    n_octal = str(oct(n))[2:]
    n_hex = str(hex(n))[2:]
    n_bin = str(bin(n))[2:]
    print(n_decimal, n_octal, n_hex, n_bin)

int_representations(25)

