
def five_consecutives_in_list(n):
    result = [[i for i in range(j-4, j+1)] for j in range(5, n+1, 5)]
    #   or
    result = [[i + 5*j for i in range(1,6)] for j in range(n//5)]
    print(result)

five_consecutives_in_list(20)
