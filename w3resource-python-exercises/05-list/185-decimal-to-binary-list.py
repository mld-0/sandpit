
def decimal_to_binary_list(n):
    result = list(int(x) for x in bin(n)[2:])
    print(result)

decimal_to_binary_list(8)
decimal_to_binary_list(45)
decimal_to_binary_list(100)
